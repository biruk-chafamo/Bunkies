import 'package:bunkies/data/user.dart';
import 'package:flutter/material.dart';

class RoomateRecCard extends StatelessWidget {
  final User user;
  const RoomateRecCard({Key? key, required this.user}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
          shape: BoxShape.rectangle,
          boxShadow: [BoxShadow(offset: Offset(2, 2), blurRadius: 5)],
          color: Colors.blue,
          borderRadius: BorderRadius.all(Radius.circular(10))),
      width: 100,
      height: 100,
      child: Column(
        children: [Text(user.username)],
      ),
    );
  }
}
