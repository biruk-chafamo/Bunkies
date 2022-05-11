import 'dart:convert';

import 'package:collection/collection.dart';

class User {
  final String username;
  final List<User> connections;

  User(
    this.username,
    this.connections,
  );

  User copyWith({
    String? username,
    List<User>? connections,
  }) {
    return User(
      username ?? this.username,
      connections ?? this.connections,
    );
  }

  Map<String, dynamic> toMap() {
    final result = <String, dynamic>{};

    result.addAll({'username': username});
    result.addAll({'connections': connections.map((x) => x.toMap()).toList()});

    return result;
  }

  factory User.fromMap(Map<String, dynamic> map) {
    return User(
      map['username'] ?? '',
      List<User>.from(map['connections']?.map((x) => User.fromMap(x))),
    );
  }

  String toJson() => json.encode(toMap());

  factory User.fromJson(String source) => User.fromMap(json.decode(source));

  @override
  String toString() => 'User(username: $username, connections: $connections)';

  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;
    final listEquals = const DeepCollectionEquality().equals;

    return other is User &&
        other.username == username &&
        listEquals(other.connections, connections);
  }

  @override
  int get hashCode => username.hashCode ^ connections.hashCode;
}
