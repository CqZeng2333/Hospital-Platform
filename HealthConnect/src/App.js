import React, { Component } from "react";
import {
  StyleSheet,
  Text,
  Image,
  View
} from 'react-native';
import GoogleLoginComponent from "./googlebutton.component";

class App extends Component {
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.brand}>
            <Image
              style={styles.logo}
              source={require('../assets/logo.png')}
            />
            <Text style={styles.brandName}> Health Connect</Text>
        </Text>
        <GoogleLoginComponent />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
//    padding: 20,
    backgroundColor: "aliceblue",
  },
  brand: {
    height: 150,
  },
  logo: {
    width: 80,
    height: 80,
    alignSelf: "flex-start",
  },
  brandName: {
    color: 'goldenrod',
    fontWeight: 'bold',
    fontSize: 36,
  },
})

export default App;

//import React from 'react';
//import type {Node} from 'react';
//import {
//  SafeAreaView,
//  ScrollView,
//  StatusBar,
//  StyleSheet,
//  Text,
//  useColorScheme,
//  View,
//} from 'react-native';
//
//import {
//  Colors,
//  DebugInstructions,
//  Header,
//  LearnMoreLinks,
//  ReloadInstructions,
//} from 'react-native/Libraries/NewAppScreen';
//
//const Section = ({children, title}): Node => {
//  const isDarkMode = useColorScheme() === 'dark';
//  return (
//    <View style={styles.sectionContainer}>
//      <Text
//        style={[
//          styles.sectionTitle,
//          {
//            color: isDarkMode ? Colors.white : Colors.black,
//          },
//        ]}>
//        {title}
//      </Text>
//      <Text
//        style={[
//          styles.sectionDescription,
//          {
//            color: isDarkMode ? Colors.light : Colors.dark,
//          },
//        ]}>
//        {children}
//      </Text>
//    </View>
//  );
//};
//
//const App: () => Node = () => {
//  const isDarkMode = useColorScheme() === 'dark';
//
//  const backgroundStyle = {
//    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
//  };
//
//  return (
//    <SafeAreaView style={backgroundStyle}>
//      <StatusBar barStyle={isDarkMode ? 'light-content' : 'dark-content'} />
//      <ScrollView
//        contentInsetAdjustmentBehavior="automatic"
//        style={backgroundStyle}>
//        <Header />
//        <View
//          style={{
//            backgroundColor: isDarkMode ? Colors.black : Colors.white,
//          }}>
//          <Section title="Step One">
//            Edit <Text style={styles.highlight}>App.js</Text> to change this
//            screen and then come back to see your edits.
//          </Section>
//          <Section title="See Your Changes">
//            <ReloadInstructions />
//          </Section>
//          <Section title="Debug">
//            <DebugInstructions />
//          </Section>
//          <Section title="Learn More">
//            Read the docs to discover what to do next:
//          </Section>
//          <LearnMoreLinks />
//        </View>
//      </ScrollView>
//    </SafeAreaView>
//  );
//};
//
//const styles = StyleSheet.create({
//  sectionContainer: {
//    marginTop: 32,
//    paddingHorizontal: 24,
//  },
//  sectionTitle: {
//    fontSize: 24,
//    fontWeight: '600',
//  },
//  sectionDescription: {
//    marginTop: 8,
//    fontSize: 18,
//    fontWeight: '400',
//  },
//  highlight: {
//    fontWeight: '700',
//  },
//});
//
//export default App;
