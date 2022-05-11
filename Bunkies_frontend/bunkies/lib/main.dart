// import 'dart:html';

import 'package:bunkies/constants/constants.dart';
import 'package:bunkies/screens/home.dart';
import 'package:bunkies/screens/welcome.dart';
import 'package:bunkies/theme/custom_theme.dart';
import 'package:bunkies/widgets/welcome_app_bar.dart';
import 'package:bunkies/widgets/welcome_drawer.dart';
import 'package:flutter/material.dart';

void main(List<String> args) {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        drawer: const WelcomeDrawer(),
        appBar: welcomeAppBar,
        body: const Welcome(),
      ),
      theme: CustomTheme.lightTheme,
    );
  }
}
