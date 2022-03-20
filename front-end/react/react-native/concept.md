- overall:

  - react native cant talk to native API
  - write JS code and share it to IOS and Android
  - IOS: Swift | Objective-C
  - Android: Java | Kotlin
  - Expo CLI:
    - a set of tools and a framework that sits on top of react native
    - cant work directly with the native API
    - don't contain ios and android folder
  - React-native CLI:
    - install must have some config like: add file [local.properties] to app folder
  - to use JSX must import React from 'react' because JSX is included in the React library

- Component:

  - View, SafeAreaView: View is the basic building block of UI
  - Text:
    - Attribute(s): numberOfLines={number}, onPres={function(){}}
  - Image:
    - Attribute(s): source={[require('RelativeURL')]|[{uri:URL_link,width:...,height:...}]}
    - When load local image doesn't need to specify dimensions because the require function read the metadata about imgs
  - Stylesheet.create({})
    - will validate property of object will be created
  - Platform: Platform.OS === 'android' ? StatusBar.currentHeight : 0
  - Dimensions:
    - Dimension.get('screen')
    - Detect device dimensions: @react-native-community/hooks
  - FlatList: chỉ render những thành phần được hiển thị tới người dùng
  - ScrollView: render tất cả các component cùng 1 lúcetting

- Concept:
  - Props: dùng để customize React components bằng cách truyền giá trị vào các component cần customize
  - state:
    - khai báo trong constructor, như private variable của class đó
    - thay đổi state: this.setState(previousState => ({ state_name: new_value }))

- TERM
  - emulator = trình giả lập (eg: Bluestack) (giả lập cả phần cứng lẫn phần mềm)
  - simulator = mô phỏng (chỉ giả lập phần mềm)
  - eject = đẩy ra
  - AVD = android virtual device
  - ADB = android debug brigde
  - Ctrl + M = open Developer menu
  - Fast Fresh = most edits should be visible within a second or two
  - metro bundler: JavaScript bundler that ships with React Native

???

- widgets
