import { createNativeStackNavigator } from "@react-navigation/native-stack";
import React from "react";
import LogIn from "../screens/LogIn";
import SignUp from "../screens/SignUp";
import Welcome from "../screens/Welcome";

const Stack = createNativeStackNavigator();

export default function LoggedOutNav() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Welcome" component={Welcome} />
      <Stack.Screen name="LogIn" component={LogIn} />
      <Stack.Screen name="SignUp" component={SignUp} />
    </Stack.Navigator>
  );
}
