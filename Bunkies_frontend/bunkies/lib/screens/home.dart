import 'package:bunkies/constants/constants.dart';
import 'package:bunkies/data/user.dart';
import 'package:flutter/material.dart';
import 'package:bunkies/widgets/roomate_rec_card.dart';

class Home extends StatelessWidget {
  Home({Key? key}) : super(key: key);
  final User biruk = User('Biruk', []);
  final User sosi = User('Sosi', []);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          color: primaryTextColor,
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: [for (var i = 0; i < 15; i += 1) i]
                  .map((child) => Padding(
                        padding: const EdgeInsets.all(8),
                        child: RoomateRecCard(
                          user: biruk,
                        ),
                      ))
                  .toList(),
            ),
          )
        ],
      ),
    );
  }
}
