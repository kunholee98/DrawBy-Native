# 정리

### Navigator

[reactNavigation](http://reactnavigation.org/)

1. Stack

내비게이터는 라우터와 동일한 목적으로 사용된다.
스택 내비게이터는 내비게이터에 스크린이 쌓이는 순서대로 보인다. (마치 카드 뭉치 중에서 가장 위의 카드만 볼 수 있는 것처럼.)
새로운 화면으로 넘어가게 되면 화면이 '이동'하는 것이 아닌, 그 위에 쌓이는 느낌. (뒤로가기 구현 가능)
그래서 이전 페이지의 정보가 위에 뜨고, 제스처도 적용된다.

- How to use..

```javascript
import {createStackNavigator} from "@react-navigation/stack";
import Nav1 from "./Nav1";
const Stack = createStackNavigator();

export default function Nav() {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Nav1" component={Nav1}>
                <Stack.Screen name="Nav2" component={Nav2}>
            </Stack.Navigator>
        </NavigationContainer>
    )
}
```

##### Navigator's props

- initialRouteName: 첫 스크린을 지정할 수 있음 (미지정 시 가장 위의 스크린이 첫 페이지)
- mode: 'card' or 'modal' (카드는 오른쪽에서, 모달은 아래쪽에서 다음 페이지가 넘어옴)
- headerMode: 페이지 제목과 뒤로가기 버튼이 있는 헤더가 스크린이 변경될 때 보이는 모션이 바뀜.
- screenOptions: 각 스크린에 적용할 수 있는 옵션들을 한번에 적용.

### Button

React Native에서 버튼 만들기

1. TouchableOpacity

: 텍스트를 눌렀을 때, 투명하게 바뀌면서 누르는 느낌을 주는 방법

```javascript
import { TouchableOpacity } from "react-native";
export default function Nav2({ navigation }) {
  return (
    <TouchableOpacity onPress={() => navigation.navigate("Nav1")}>
      <View>
        <Text>This is Button</Text>
      </View>
    </TouchableOpacity>
  );
}
// Nav1으로 화면이 이동되는 버튼
// Navigator.Screen에 부여한 이름과 동일한 페이지로 이동.
```

2. TouchableWithoutFeedback

TouchblaOpacitiy랑 똑같지만, 눌렀을 때 시각적인 피드백이 없다.

보통 키보드를 없에기 위해서 배경을 누르는 것을 구현하고자 할때 사용한다. (Keyboard.dismiss())

3. ActivityIndicator

로딩할 때 많이 보던 그 동그라미 돌아가는 거를 보여주는 컴포넌트

보통 버튼을 눌렀을 때, loading prop을 받아 만약 loading === true라면 로딩 컴포넌트 실행

### Styled

React와 동일하게 사용되는 styled.

하지만 사용을 위해서는 이와 같이 import 해주어야 한다.

```javascript
import styled from "styled-components/native";
```

##### 특징들

- **flex: 1** : 이는 column이 하나라는 것을 의미하는 native 만의 요소
- React, CSS와 달리 부모의 font를 설정해주어도 자식 컴포넌트는 이를 상속받지 않는다. (Text에 관한 설정은 모두 Text 컴포넌트 안에서 설정)

### TextInput

텍스트를 적을 수 있는 박스

```javascript
import { TextInput } from "react-native";
import { useRef } from "React";
<TextInput></TextInput>;
```

1. ref, onSubmitEditing을 이용하여 enter를 눌렀을 때 다음 입력칸으로 넘어갈 수 있음

```javascript
const nextRef = useRef();
const onNext = () => {
  nextRef.current?.focus();
};
<TextInput onSubmitEditing={onNext}>last</TextInput>;
<TextInput ref={nextRef}>next</TextInput>;
```

### KeyboardAvoidingView

키보드가 나타났을 때 화면이 키보드에 가려지지 않도록 요소를 위로 자동적으로 올려주는 컴포넌트

1. behavior: 어떤 것을 기준으로 위로 올릴 것인가 ex) padding, position
2. keyboardVerticalOffset={Platform.OS === 'ios' ? 30 : 0} : os가 ios라면 vertical offset을 30만큼 (os마다 설정 가능)

### 백엔드 localhost를 바깥으로 노출하는 방법

1. ngrok
2. localtunnel

```shell
npx localtunnel --port 4000
```
