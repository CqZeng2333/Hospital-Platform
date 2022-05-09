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
