import 'package:bunkies/screens/home.dart';
import 'package:bunkies/theme/custom_theme.dart';
import 'package:flutter/material.dart';
import 'package:bunkies/constants/constants.dart';

class Welcome extends StatelessWidget {
  const Welcome({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(welcomePadding),
      child: Align(
        alignment: Alignment.topCenter,
        child: Wrap(
          runSpacing: welcomePadding,
          spacing: 4 * welcomePadding,
          children: [
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Text(
                  "Find the perfect Bunky",
                  style: Theme.of(context).textTheme.headline1,
                ),
                Text(
                  "List your preferences and we'll match you with the perfect roommate",
                  style: Theme.of(context).textTheme.headline5,
                ),
                Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    TextButton(
                      child: const Text('Sign Up'),
                      onPressed: () => {},
                    ),
                    OutlinedButton(
                      child: const Text('Log in'),
                      onPressed: () => {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => Home()),
                        )
                      },
                    ),
                  ]
                      .map(
                        (child) => Padding(
                          padding: const EdgeInsets.all(largeButtonPadding),
                          child: child,
                        ),
                      )
                      .toList(),
                ),
              ]
                  .map(
                    (child) => Padding(
                      padding: const EdgeInsets.all(15),
                      child: child,
                    ),
                  )
                  .toList(),
            ),
            Container(
              child: const Image(
                image: AssetImage('sample.png'),
              ),
              decoration: BoxDecoration(boxShadow: [
                BoxShadow(
                  color: Colors.grey.withOpacity(0.5),
                  spreadRadius: 5,
                  blurRadius: 15,
                  offset: const Offset(0, 3), // changes position of shadow
                ),
              ]),
            ),
          ],
        ),
      ),
    );
  }
}
