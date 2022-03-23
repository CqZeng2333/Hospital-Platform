from deepspeech import Model
from scipy.io import wavfile
import threading
import queue

def get_deepspeech_model():
    model_path = 'chat/model/deepspeech-0.9.3-models.pbmm'
    ars = Model(model_path)
    return ars

threadLock = threading.Lock()
queueLock = threading.Lock()
workQueue = queue.Queue(10)
exitFlag = 0
model = get_deepspeech_model()
error_msg = ''

def deepspeech_process_wav_file(q, translates):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            wav_file = q.get()
            queueLock.release()

            # Process data
            if wav_file:
                _, data = wavfile.read(wav_file)
                translate_text = model.stt(data)
            else:
                translate_text = error_msg
            
            # Add into the result set
            threadLock.acquire()
            translates.append(translate_text)
            threadLock.release()
        else:
            queueLock.release()

class WavThread (threading.Thread):
    def __init__(self, threadID, name, translates:list, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.translates = translates
        self.q = q
    
    def run(self):
        deepspeech_process_wav_file(self.q, self.translates)

# To translate multiple wav files to text
# using multi-thread and Queue
def process_wav_files(wav_files, error_message):
    global exitFlag
    exitFlag = 0
    global error_msg
    error_msg = error_message
    translates = []

    # Start threads (at most 8)
    threads = []
    threadID = 1
    if len(wav_files) > 8:
        thread_num = 8
    else:
        thread_num = len(wav_files)
    for i in range(thread_num):
        thread = WavThread(threadID, 'Thread-' + str(i + 1), translates, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1
    
    # Add in data for processing
    for i in range(len(wav_files)):
        queueLock.acquire()
        if workQueue.full():
            i -= 1
        else:
            workQueue.put(wav_files[i])
        queueLock.release()

    # Wait for jobs to finish
    while not workQueue.empty():
        pass
    
    exitFlag = 1
    for t in threads:
        t.join()
    
    return translates