import 'package:flutter/material.dart';
import 'api_service.dart'; // Correct relative path
import 'dart:convert';
import 'package:http/http.dart' as http; // Need http package for the controllers check

class GenericCrudScreen extends StatefulWidget {
  final String title;
  final String endpoint;
  final String titleField;
  final String subtitleField;
  final List<String> fields;

  const GenericCrudScreen({
    super.key,
    required this.title,
    required this.endpoint,
    required this.titleField,
    required this.subtitleField,
    required this.fields,
  });

  @override
  _GenericCrudScreenState createState() => _GenericCrudScreenState();
}

class _GenericCrudScreenState extends State<GenericCrudScreen> {
  // Use lazy initialization or fix the constructor if ApiService requires params
  // Since ApiService only uses baseUrl from its hardcoded field, this is safe.
  final ApiService api = ApiService();
  List<dynamic> items = [];
  bool isLoading = true;

  // List of ALL possible foreign key fields across all apps (HR, Infra, Poultry, Assets)
  static const List<String> fkFields = [
    "employee", "branch", "address", "manager", "farm", "house",
    "owner", "building", "batch", "breed", "vaccine", "assigned_to",
    "manager_employee", "approver", "changed_by"
  ];

  @override
  void initState() {
    super.initState();
    refreshData();
  }

  Future<void> refreshData() async {
    if (!mounted) return;
    setState(() => isLoading = true);
    final data = await api.fetch(widget.endpoint);
    if (!mounted) return;
    setState(() {
      items = data;
      isLoading = false;
    });
  }

  // --- FORM LOGIC ---
  void showForm({Map<String, dynamic>? item}) {
    Map<String, TextEditingController> controllers = {};
    for (String field in widget.fields) {
      controllers[field] = TextEditingController(
        text: item != null && item[field] != null ? item[field].toString() : '',
      );
    }

    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: Text(item == null ? "Add New ${widget.title}" : "Edit ${widget.title}"),
        content: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: widget.fields.map((field) {
              bool isDateField = field.toLowerCase().contains("date") || field.toLowerCase() == "dob";

              return Padding(
                padding: const EdgeInsets.only(bottom: 8.0),
                child: TextField(
                  controller: controllers[field],
                  readOnly: isDateField,
                  keyboardType: fkFields.contains(field) ? TextInputType.number : TextInputType.text,
                  decoration: InputDecoration(
                    labelText: field.toUpperCase().replaceAll('_', ' '),
                    border: const OutlineInputBorder(),
                    suffixIcon: isDateField ? const Icon(Icons.calendar_today) : null,
                  ),
                  onTap: isDateField ? () async {
                    DateTime? pickedDate = await showDatePicker(
                      context: context,
                      initialDate: DateTime.now(),
                      firstDate: DateTime(1950),
                      lastDate: DateTime(2100),
                    );
                    if (pickedDate != null) {
                      String formattedDate = pickedDate.toIso8601String().split('T')[0];
                      controllers[field]!.text = formattedDate;
                    }
                  } : null,
                ),
              );
            }).toList(),
          ),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text("Cancel")),
          ElevatedButton(
            onPressed: () async {
              Map<String, dynamic> data = {};
              controllers.forEach((key, controller) {
                // Determine if field should be sent as integer ID or string
                if (fkFields.contains(key) && controller.text.isNotEmpty) {
                  // Try to parse as int for Foreign Key IDs
                  data[key] = int.tryParse(controller.text) ?? controller.text;
                } else if (fkFields.contains(key) && controller.text.isEmpty) {
                  data[key] = null; // Send null for empty FK fields
                } else {
                  data[key] = controller.text;
                }
              });

              bool success;
              if (item == null) {
                success = await api.create(widget.endpoint, data);
              } else {
                success = await api.update(widget.endpoint, item['id'], data);
              }

              if (success) {
                if(mounted) Navigator.pop(ctx);
                refreshData();
                if(mounted) ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text("Success!")));
              } else {
                if(mounted) ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text("Failed. Check Console.")));
              }
            },
            child: const Text("Save"),
          )
        ],
      ),
    );
  }

  void deleteItem(int id) async {
    bool? confirm = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text("Delete Item?"),
        content: const Text("This action cannot be undone."),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text("Cancel")),
          TextButton(onPressed: () => Navigator.pop(ctx, true), child: const Text("Delete", style: TextStyle(color: Colors.red))),
        ],
      ),
    );

    if (confirm == true) {
      bool success = await api.delete(widget.endpoint, id);
      if (success) refreshData();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.teal,
        child: const Icon(Icons.add),
        onPressed: () => showForm(),
      ),
      body: isLoading
          ? const Center(child: CircularProgressIndicator())
          : items.isEmpty
          ? Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.search_off, size: 50, color: Colors.grey),
            Text("No items found for ${widget.title}. Tap '+' to add one."),
            const SizedBox(height: 10),
            ElevatedButton(onPressed: refreshData, child: const Text("Refresh"))
          ],
        ),
      )
          : ListView.builder(
        itemCount: items.length,
        itemBuilder: (ctx, i) {
          final item = items[i];

          String titleText = item[widget.titleField]?.toString() ?? "Unknown";
          String subtitleText = item[widget.subtitleField]?.toString() ?? "";

          return Card(
            margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.teal.shade100,
                child: Text(
                  titleText.isNotEmpty && titleText != "Unknown" ? titleText.substring(0, 1).toUpperCase() : "?",
                  style: TextStyle(color: Colors.teal.shade900),
                ),
              ),
              title: Text(titleText, style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: subtitleText.isNotEmpty ? Text(subtitleText) : null,
              trailing: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  IconButton(icon: const Icon(Icons.edit, color: Colors.blue), onPressed: () => showForm(item: item)),
                  IconButton(icon: const Icon(Icons.delete, color: Colors.red), onPressed: () => deleteItem(item['id'])),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}