import React, { Component } from "react";
import {
   FlatList,
   StyleSheet,
   Text,
   View,
   TextInput,
   Button,
   Dimensions,
} from 'react-native';

export default class App extends Component {
    state = {
        chatItems: [
//          "Hello!",
//          "How are you today?",
//          "When can we have an appointment?",
        ]
    }
  render() {
      return (
        <View style={styles.container}>
          <FlatList
              data={this.state.chatItems}
              renderItem={({item}) => <Text style={styles.item}>{item}</Text>
              }
          />
          <><TextInput style={styles.input} />
          <Button title="Send" style={styles.send} /></>
        </View>
      );
    }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  item: {
    marginTop: 10,
    marginLeft: 10,
    padding: 8,
    fontSize: 14,
    width:200,
    color: "black",
    borderWidth: 3,
    borderRadius: 18,
    backgroundColor: "beige",
  },
  input: {
    height: 40,
    width: Dimensions.get('window').width - 12,
    margin: 8,
    borderWidth: 1,
    padding: 10,
    alignSelf: "flex-end",
  },
  send: {
    height: 40,
    borderRadius: 20,
    backgroundColor: "beige",
    alignSelf: "flex-end",
  },
});