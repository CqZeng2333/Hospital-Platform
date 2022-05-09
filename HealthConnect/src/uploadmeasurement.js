import React, { Component } from "react";
import {
   FlatList,
   StyleSheet,
   Text,
   View,
   TextInput,
} from 'react-native';

export default class MeasurementInput extends Component {
    state = {
        measureItems: [
          "Temperature",
          "Systolic Blood Pressure",
          "Diastolic Blood Pressure",
          "Pulse",
          "Oximeter",
          "Weight",
          "Glucometer"
        ]
    }
  render() {
      return (
        <View style={styles.container}>
          <FlatList
                  data={[
                    {key: this.state.measureItems[0]},
                    {key: this.state.measureItems[1]},
                    {key: this.state.measureItems[2]},
                    {key: this.state.measureItems[3]},
                    {key: this.state.measureItems[4]},
                    {key: this.state.measureItems[5]},
                    {key: this.state.measureItems[6]},
                  ]}
                  renderItem={({item}) => <><Text style={styles.item}>{item.key}</Text>
                    <TextInput style={styles.input} /></>
                  }
          />
        </View>
      );
    }



}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  alignTextCenter: {
    textAlign: 'center',
    justifyContent: 'center',
  },
  item: {
    padding: 10,
    fontSize: 18,
    height: 44,
    color: "black",
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  }
});