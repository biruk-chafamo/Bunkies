import 'package:bunkies/constants/constants.dart';
import 'package:flutter/material.dart';

class WelcomeDrawer extends StatelessWidget {
  const WelcomeDrawer({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Builder(builder: (BuildContext context) {
      return Drawer(
        // Add a ListView to the drawer. This ensures the user can scroll
        // through the options in the drawer if there isn't enough vertical
        // space to fit everything.
        child: ListView(
          // Important: Remove any padding from the ListView.
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              decoration: const BoxDecoration(
                color: backgroundButtonColor,
              ),
              child: Text(
                'Bunkies',
                style: Theme.of(context)
                    .textTheme
                    .headline5
                    ?.copyWith(color: primaryButtonColor),
              ),
            ),
            ListTile(
              title: const Text('Overview'),
              onTap: () {},
            ),
            ListTile(
              title: const Text('Pricing'),
              onTap: () {},
            ),
          ],
        ),
      );
    });
  }
}
