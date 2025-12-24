import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // ⚠️ BASE URL: Ensure this is correct for your Django setup.
  // Assuming: Django is running on http://10.0.2.2:8000/ and the API router is accessible at /api/
  final String baseUrl = "http://10.0.2.2:8000/api";

  String? _sessionCookie;
  String? _csrfToken;

  // Helper function to create headers including auth/csrf
  Map<String, String> _getHeaders() {
    Map<String, String> headers = {"Content-Type": "application/json"};
    if (_sessionCookie != null) {
      headers['Cookie'] = _sessionCookie!;
    }
    if (_csrfToken != null) {
      headers['X-CSRFToken'] = _csrfToken!;
    }
    return headers;
  }

  // GET (Read) - With Diagnostics
  Future<List<dynamic>> fetch(String endpoint) async {
    try {
      final url = Uri.parse('$baseUrl/$endpoint/');
      print("🔌 Fetching: $url");

      final response = await http.get(url);

      if (response.statusCode == 200) {
        final dynamic decodedData = json.decode(utf8.decode(response.bodyBytes));

        if (decodedData is Map<String, dynamic> && decodedData.containsKey('results')) {
          print("✅ Success: $endpoint");
          return decodedData['results'];
        }

        if (decodedData is List) {
          print("✅ Success: $endpoint");
          return decodedData;
        }

        // Diagnostic return for empty lists or unexpected data structure
        throw Exception('Received unexpected data structure from API. Status 200.');

      } else {
        // Diagnostic: Throw an error with the HTTP status code
        throw Exception('HTTP Error ${response.statusCode}: ${response.body}');
      }
    } catch (e) {
      // Diagnostic: Throw a connection or decoding error
      throw Exception('Connection/Runtime Error for $endpoint: ${e.toString()}');
    }
  }

  // POST (Add)
  Future<bool> create(String endpoint, Map<String, dynamic> data) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/$endpoint/'),
        headers: _getHeaders(),
        body: json.encode(data),
      );

      if (response.statusCode == 201) {
        return true;
      } else {
        print("POST FAILED at $endpoint");
        print("Status Code: ${response.statusCode}");
        print("Server Response: ${response.body}");
        return false;
      }
    } catch (e) {
      print("Error creating in $endpoint: $e");
      return false;
    }
  }

  // PUT (Edit)
  Future<bool> update(String endpoint, int id, Map<String, dynamic> data) async {
    try {
      final response = await http.put(
        Uri.parse('$baseUrl/$endpoint/$id/'),
        headers: _getHeaders(),
        body: json.encode(data),
      );

      if (response.statusCode == 200) {
        return true;
      } else {
        print("PUT FAILED at $endpoint ID: $id");
        print("Status Code: ${response.statusCode}");
        print("Server Response: ${response.body}");
        return false;
      }
    } catch (e) {
      print("Error updating $endpoint: $e");
      return false;
    }
  }

  // DELETE (Remove)
  Future<bool> delete(String endpoint, int id) async {
    try {
      final response = await http.delete(
        Uri.parse('$baseUrl/$endpoint/$id/'),
        headers: _getHeaders(),
      );
      if (response.statusCode == 204) {
        return true;
      } else {
        print("DELETE Error: ${response.statusCode} - ${response.body}");
        return false;
      }
    } catch (e) {
      print("Error deleting $endpoint: $e");
      return false;
    }
  }
}