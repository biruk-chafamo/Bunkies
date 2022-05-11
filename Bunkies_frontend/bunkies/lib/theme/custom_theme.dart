import 'package:bunkies/constants/constants.dart';
import 'package:flutter/material.dart';

class CustomTheme {
  static ThemeData get lightTheme {
    return ThemeData(
      textTheme: const TextTheme(
        headline1: TextStyle(
          fontSize: headline1Font,
          color: primaryTextColor,
        ),
        headline5: TextStyle(
          fontSize: headline5Font,
          color: secondaryTextColor,
        ),
      ),
      textButtonTheme: TextButtonThemeData(
        style: textButtonThemeData(inverted: false).style,
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: textButtonThemeData(inverted: true).style,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: Colors.white,
        elevation: 1,
      ),
    );
  }
}

TextButtonThemeData textButtonThemeData({bool inverted = false}) {
  return TextButtonThemeData(
    style: TextButton.styleFrom(
      primary: inverted ? backgroundButtonColor : primaryButtonColor,
      backgroundColor: inverted ? primaryButtonColor : backgroundButtonColor,
      padding: const EdgeInsets.symmetric(
        vertical: 2 * largeButtonPadding,
        horizontal: 8 * largeButtonPadding,
      ),
      textStyle: const TextStyle(
        fontSize: largeButtonFontSize,
      ),
    ),
  );
}
