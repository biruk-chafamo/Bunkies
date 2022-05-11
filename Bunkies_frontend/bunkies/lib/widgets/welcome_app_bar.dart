import 'package:bunkies/constants/constants.dart';
import 'package:flutter/material.dart';

PreferredSizeWidget welcomeAppBar = AppBar(
  title: Builder(builder: (BuildContext context) {
    return Text(
      'Bunkies',
      style: Theme.of(context).textTheme.bodyLarge?.copyWith(
            color: secondaryTextColor,
            fontWeight: FontWeight.bold,
          ),
    );
  }),
  centerTitle: false,
  leading: Builder(
    builder: (BuildContext context) {
      return IconButton(
        icon: const Icon(
          Icons.menu,
          color: primaryTextColor,
        ),
        onPressed: () {
          Scaffold.of(context).openDrawer();
        },
      );
    },
  ),
);
