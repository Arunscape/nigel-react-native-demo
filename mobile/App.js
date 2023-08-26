import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View} from 'react-native';
import { useEffect, useState } from 'react';
//import EventSource from 'react-native-sse';
//let's just try using websockets since react native supports that officially


export default function App() {

  const [message, setMessage] = useState('');

  //useEffect(() => {
  //  const eventSource = new EventSource('http://localhost:8000/sse');
  //  eventSource.onmessage = (event) => {
  //    setMessage(event.data);
  //    console.log(event);
  //  };

  //  return () => {
  //    eventSource.close();
  //  }
  //}, [])

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws')
    ws.onopen = () => {}
    ws.onmessage = (event) => {
      setMessage(event.data);
      console.log(event);
    };

    ws.onerror = (event) => {
      console.error(event);
    }
    ws.onclose = (event) => {
      console.log(event);
    }

    return () => {
      ws.close();
    }
  }, [])

  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <StatusBar style="auto" />
      <Text>The number below comes from the server</Text>
      <Text>{message}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
