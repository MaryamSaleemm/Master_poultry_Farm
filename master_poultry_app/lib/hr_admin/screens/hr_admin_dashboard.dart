import 'package:flutter/material.dart';
// If you need to use the generic_crud file shown in your image:
// import '../services/generic_crud.dart';

class HrAdminDashboard extends StatelessWidget {
  const HrAdminDashboard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("HR & Admin Dashboard"),
        backgroundColor: Colors.blueAccent,
      ),
      body: Container(
        padding: const EdgeInsets.all(16.0),
        child: GridView.count(
          crossAxisCount: 2, // 2 columns
          crossAxisSpacing: 10,
          mainAxisSpacing: 10,
          children: [
            // Option 1: Manage Staff
            _buildDashboardCard(
                icon: Icons.people,
                title: "Manage Staff",
                onTap: () {
                  // Navigation to Staff List will go here
                }
            ),

            // Option 2: Payroll
            _buildDashboardCard(
                icon: Icons.attach_money,
                title: "Payroll",
                onTap: () {
                  // Navigation to Payroll will go here
                }
            ),

            // Option 3: Attendance
            _buildDashboardCard(
                icon: Icons.calendar_today,
                title: "Attendance",
                onTap: () {
                  // Navigation to Attendance will go here
                }
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDashboardCard({required IconData icon, required String title, required VoidCallback onTap}) {
    return Card(
      elevation: 4,
      child: InkWell(
        onTap: onTap,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 40, color: Colors.blueAccent),
            const SizedBox(height: 10),
            Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}