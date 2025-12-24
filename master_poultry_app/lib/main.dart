import 'package:flutter/material.dart';
import 'splash_screen.dart'; // File: lib/splash_screen.dart
// Corrected import path: Assumes generic_crud.dart is in lib/services/
// If it's in lib/hr_admin/services/, change this line to:
// import 'hr_admin/services/generic_crud.dart';
import 'hr_admin/services/generic_crud.dart';

void main() {
  runApp(const MasterPoultryApp());
}

class MasterPoultryApp extends StatelessWidget {
  const MasterPoultryApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      // The home property points directly to the SplashScreen for initial load
      home: SplashScreen(),
    );
  }
}

// ==========================================
// 1. MASTER POULTRY HOME (Sidebar & App Switcher)
// ==========================================

class MasterPoultryHome extends StatefulWidget {
  const MasterPoultryHome({super.key});

  @override
  _MasterPoultryHomeState createState() => _MasterPoultryHomeState();
}

class _MasterPoultryHomeState extends State<MasterPoultryHome> {
  // Start on Assets for testing purposes
  int _selectedAppIndex = 3;

  final List<String> _appTitles = [
    "HR & Admin",
    "Farm Infrastructure",
    "Poultry Operations",
    "Assets & Inventory",
    "Supply & Finance"
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(_appTitles[_selectedAppIndex]),
        backgroundColor: Colors.teal,
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(color: Colors.teal),
              child: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.home_work, color: Colors.white, size: 50),
                    SizedBox(height: 10),
                    Text(
                      "Master Poultry Farm",
                      style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.bold),
                    ),
                  ],
                ),
              ),
            ),
            _buildDrawerItem(0, Icons.people, "HR & Admin"),
            _buildDrawerItem(1, Icons.fence, "Farm Infrastructure"),
            _buildDrawerItem(2, Icons.egg, "Poultry Operations"),
            _buildDrawerItem(3, Icons.inventory_2, "Assets & Inventory"),
            _buildDrawerItem(4, Icons.attach_money, "Supply & Finance"),
          ],
        ),
      ),
      body: _buildBody(),
    );
  }

  Widget _buildDrawerItem(int index, IconData icon, String title) {
    return ListTile(
      leading: Icon(icon, color: _selectedAppIndex == index ? Colors.teal : Colors.grey),
      title: Text(
        title,
        style: TextStyle(
          color: _selectedAppIndex == index ? Colors.teal : Colors.black,
          fontWeight: _selectedAppIndex == index ? FontWeight.bold : FontWeight.normal,
        ),
      ),
      selected: _selectedAppIndex == index,
      onTap: () {
        setState(() => _selectedAppIndex = index);
        Navigator.pop(context);
      },
    );
  }

  Widget _buildBody() {
    switch (_selectedAppIndex) {
      case 0: return const HRAdminAppView();
      case 1: return const FarmInfrastructureAppView();
      case 2: return const PoultryOperationsAppView();
      case 3: return const AssetsAppView();
      case 4: return const PlaceholderApp(title: "Supply & Finance");
      default: return const Center(child: Text("Select an App"));
    }
  }
}

// ==========================================
// 2. APP 4: ASSETS & INVENTORY (CORRECT LOGIC)
// ==========================================

class AssetsAppView extends StatelessWidget {
  const AssetsAppView({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 4,
      child: Column(
        children: [
          Container(
            color: Colors.teal.shade700,
            child: const TabBar(
              isScrollable: true,
              indicatorColor: Colors.white,
              labelColor: Colors.white,
              unselectedLabelColor: Colors.white70,
              tabs: [
                Tab(icon: Icon(Icons.people_alt), text: "Owners"),
                Tab(icon: Icon(Icons.apartment), text: "Buildings"),
                Tab(icon: Icon(Icons.gavel), text: "Compliance"),
                Tab(icon: Icon(Icons.handyman), text: "Inventory"),
              ],
            ),
          ),
          const Expanded(
            child: TabBarView(
              children: [
                AssetOwnersTab(),
                AssetBuildingsTab(),
                AssetComplianceTab(),
                PlaceholderApp(title: "Inventory Management"),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// --- ASSETS TABS ---

class AssetOwnersTab extends StatelessWidget {
  const AssetOwnersTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Basic"), Tab(text: "Contacts"), Tab(text: "Addresses")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Owner Basic", endpoint: "owners", titleField: "owner_name", subtitleField: "id", fields: const ["owner_name"]),
              GenericCrudScreen(title: "Owner Contacts", endpoint: "owner-contacts", titleField: "phone", subtitleField: "email", fields: const ["owner", "phone", "email"]),
              GenericCrudScreen(title: "Owner Addresses", endpoint: "owner-address", titleField: "street", subtitleField: "city", fields: const ["owner", "street", "city", "state_province", "postal_code", "country"]),
            ]),
          )
        ],
      ),
    );
  }
}

class AssetBuildingsTab extends StatelessWidget {
  const AssetBuildingsTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 5,
      child: Column(
        children: [
          const TabBar(isScrollable: true, labelColor: Colors.black, tabs: [Tab(text: "Basic"), Tab(text: "Location"), Tab(text: "Specs"), Tab(text: "Facilities"), Tab(text: "Management")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Building Basic", endpoint: "buildings", titleField: "building_name", subtitleField: "building_code", fields: const ["building_name", "building_code"]),
              GenericCrudScreen(title: "Building Location", endpoint: "locations", titleField: "street_address", subtitleField: "city", fields: const ["building", "street_address", "city", "country", "latitude", "longitude"]),
              GenericCrudScreen(title: "Building Specs", endpoint: "specs", titleField: "total_area", subtitleField: "construction_year", fields: const ["building", "floors", "total_area", "construction_year", "condition", "occupancy_status"]),
              GenericCrudScreen(title: "Building Facilities", endpoint: "facilities", titleField: "security_system", subtitleField: "power_backup", fields: const ["building", "parking_capacity", "power_backup", "internet_available", "security_system", "additional_notes"]),
              GenericCrudScreen(title: "Building Management", endpoint: "management", titleField: "maintenance_contact", subtitleField: "owner", fields: const ["building", "owner", "manager_employee", "maintenance_contact", "emergency_contact"]),
            ]),
          )
        ],
      ),
    );
  }
}

class AssetComplianceTab extends StatelessWidget {
  const AssetComplianceTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Permits"), Tab(text: "Licenses"), Tab(text: "Inspections")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Permits", endpoint: "permits", titleField: "permit_type", subtitleField: "expiry_date", fields: const ["building", "permit_type", "issue_date", "expiry_date", "status", "issued_by"]),
              GenericCrudScreen(title: "Licenses", endpoint: "licenses", titleField: "license_type", subtitleField: "expiry_date", fields: const ["building", "license_type", "issue_date", "expiry_date", "status"]),
              GenericCrudScreen(title: "Inspections", endpoint: "inspections", titleField: "inspection_date", subtitleField: "status", fields: const ["building", "inspection_date", "inspector_name", "report", "status"]),
            ]),
          )
        ],
      ),
    );
  }
}


// ==========================================
// 3. APP 3: POULTRY OPERATIONS (CORRECT LOGIC)
// ==========================================

class PoultryOperationsAppView extends StatelessWidget {
  const PoultryOperationsAppView({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 4,
      child: Column(
        children: [
          Container(
            color: Colors.teal.shade700,
            child: const TabBar(
              isScrollable: true,
              indicatorColor: Colors.white,
              labelColor: Colors.white,
              unselectedLabelColor: Colors.white70,
              tabs: [
                Tab(icon: Icon(Icons.group), text: "Flock"),
                Tab(icon: Icon(Icons.medical_services), text: "Health"),
                Tab(icon: Icon(Icons.egg_alt), text: "Production"),
                Tab(icon: Icon(Icons.assignment), text: "Tasks"),
              ],
            ),
          ),
          const Expanded(
            child: TabBarView(
              children: [
                PoultryFlockTab(),
                PoultryHealthTab(),
                PoultryProductionTab(),
                PoultryTasksTab(),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// --- POULTRY TABS ---

class PoultryFlockTab extends StatelessWidget {
  const PoultryFlockTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Breeds"), Tab(text: "Batches"), Tab(text: "Mortality")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Breeds", endpoint: "breeds", titleField: "breed_name", subtitleField: "category", fields: const ["breed_name", "category"]),
              GenericCrudScreen(title: "Batches", endpoint: "batches", titleField: "batch_code", subtitleField: "arrival_date", fields: const ["house", "batch_code", "breed", "quantity", "arrival_date"]),
              GenericCrudScreen(title: "Mortality", endpoint: "mortality", titleField: "date", subtitleField: "cause", fields: const ["batch", "date", "count", "cause"]),
            ]),
          )
        ],
      ),
    );
  }
}

class PoultryHealthTab extends StatelessWidget {
  const PoultryHealthTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Vaccines"), Tab(text: "Records"), Tab(text: "Vet Visits")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Vaccines", endpoint: "vaccines", titleField: "vaccine_name", subtitleField: "id", fields: const ["vaccine_name"]),
              GenericCrudScreen(title: "Vaccine Records", endpoint: "vaccine-records", titleField: "date_administered", subtitleField: "dose", fields: const ["batch", "vaccine", "date_administered", "dose"]),
              GenericCrudScreen(title: "Vet Visits", endpoint: "vet", titleField: "visit_date", subtitleField: "vet_name", fields: const ["batch", "visit_date", "vet_name", "findings"]),
            ]),
          )
        ],
      ),
    );
  }
}

class PoultryProductionTab extends StatelessWidget {
  const PoultryProductionTab({super.key});
  @override
  Widget build(BuildContext context) {
    return GenericCrudScreen(
        title: "Egg Collection",
        endpoint: "eggs",
        titleField: "date",
        subtitleField: "eggs_collected",
        fields: const ["batch", "date", "eggs_collected", "broken"]
    );
  }
}

class PoultryTasksTab extends StatelessWidget {
  const PoultryTasksTab({super.key});
  @override
  Widget build(BuildContext context) {
    return GenericCrudScreen(
        title: "Farm Tasks",
        endpoint: "tasks",
        titleField: "task",
        subtitleField: "due_date",
        fields: const ["task", "assigned_to", "due_date", "status"]
    );
  }
}


// ==========================================
// 4. APP 2: FARM INFRASTRUCTURE (CORRECT LOGIC)
// ==========================================

class FarmInfrastructureAppView extends StatelessWidget {
  const FarmInfrastructureAppView({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          Container(
            color: Colors.teal.shade700,
            child: const TabBar(
              indicatorColor: Colors.white,
              labelColor: Colors.white,
              unselectedLabelColor: Colors.white70,
              tabs: [
                Tab(icon: Icon(Icons.landscape), text: "General Info"),
                Tab(icon: Icon(Icons.home), text: "Housing"),
                Tab(icon: Icon(Icons.construction), text: "Projects & Audits"),
              ],
            ),
          ),
          const Expanded(
            child: TabBarView(
              children: [
                FarmGeneralTab(),
                FarmHousingTab(),
                FarmProjectsTab(),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// --- INFRA TABS ---

class FarmGeneralTab extends StatelessWidget {
  const FarmGeneralTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Basic"), Tab(text: "Location"), Tab(text: "Ownership")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Farm Basic", endpoint: "farms", titleField: "name", subtitleField: "description", fields: const ["farm_name", "description"]),
              GenericCrudScreen(title: "Location", endpoint: "locations", titleField: "city", subtitleField: "street_address", fields: const ["farm", "street_address", "city"]),
              GenericCrudScreen(title: "Ownership", endpoint: "ownerships", titleField: "owner_name", subtitleField: "owner_contact", fields: const ["farm", "owner_name", "owner_contact"]),
            ]),
          )
        ],
      ),
    );
  }
}

class FarmHousingTab extends StatelessWidget {
  const FarmHousingTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Houses"), Tab(text: "Specs"), Tab(text: "Utilities")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Houses", endpoint: "houses", titleField: "house_name", subtitleField: "type", fields: const ["farm", "house_name", "capacity", "type"]),
              GenericCrudScreen(title: "House Specs", endpoint: "house-specs", titleField: "ventilation_type", subtitleField: "floor_area", fields: const ["house", "floor_area", "ventilation_type"]),
              GenericCrudScreen(title: "Utilities", endpoint: "house-utilities", titleField: "water_source", subtitleField: "electricity", fields: const ["house", "electricity", "water_source"]),
            ]),
          )
        ],
      ),
    );
  }
}

class FarmProjectsTab extends StatelessWidget {
  const FarmProjectsTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Construction"), Tab(text: "Audits")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Construction", endpoint: "projects", titleField: "project_name", subtitleField: "start_date", fields: const ["farm", "project_name", "start_date", "end_date"]),
              GenericCrudScreen(title: "Audits", endpoint: "audits", titleField: "auditor_name", subtitleField: "audit_date", fields: const ["farm", "audit_date", "auditor_name", "report"]),
            ]),
          )
        ],
      ),
    );
  }
}

// ==========================================
// 5. APP 1: HR ADMIN (CORRECT LOGIC)
// ==========================================

class HRAdminAppView extends StatelessWidget {
  const HRAdminAppView({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 5,
      child: Column(
        children: [
          Container(
            color: Colors.teal.shade700,
            child: const TabBar(
              isScrollable: true,
              indicatorColor: Colors.white,
              labelColor: Colors.white,
              unselectedLabelColor: Colors.white70,
              tabs: [
                Tab(icon: Icon(Icons.dashboard), text: "Dash"),
                Tab(icon: Icon(Icons.people), text: "Profiles"),
                Tab(icon: Icon(Icons.work), text: "Operations"),
                Tab(icon: Icon(Icons.trending_up), text: "Performance"),
                Tab(icon: Icon(Icons.monetization_on), text: "Payroll"),
              ],
            ),
          ),
          const Expanded(
            child: TabBarView(
              children: [
                DashboardPlaceholder(title: "HR Dashboard"),
                EmployeeProfilesTab(),
                HROperationsTab(),
                PerformanceTab(),
                TrainingTab(),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// --- HR TABS ---

class EmployeeProfilesTab extends StatelessWidget {
  const EmployeeProfilesTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 5,
      child: Column(
        children: [
          const TabBar(isScrollable: true, labelColor: Colors.black, tabs: [
            Tab(text: "Basic"), Tab(text: "Jobs"), Tab(text: "Contacts"), Tab(text: "Addresses"), Tab(text: "Access")
          ]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Employees", endpoint: "employees", titleField: "first_name", subtitleField: "national_id", fields: const ["first_name", "last_name", "national_id", "dob"]),
              GenericCrudScreen(title: "Jobs", endpoint: "jobs", titleField: "job_title", subtitleField: "role", fields: const ["employee", "job_title", "role", "branch", "hire_date", "status", "employment_type", "work_location"]),
              GenericCrudScreen(title: "Contacts", endpoint: "contacts", titleField: "email", subtitleField: "phone", fields: const ["employee", "phone", "email", "address"]),
              GenericCrudScreen(title: "Addresses", endpoint: "addresses", titleField: "street", subtitleField: "city", fields: const ["street", "city", "state_province", "postal_code", "country"]),
              GenericCrudScreen(title: "Access", endpoint: "access", titleField: "username", subtitleField: "user_role", fields: const ["employee", "username", "user_role", "access_level"]),
            ]),
          )
        ],
      ),
    );
  }
}

class HROperationsTab extends StatelessWidget {
  const HROperationsTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Branches"), Tab(text: "Attendance"), Tab(text: "Leaves")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Branches", endpoint: "branches", titleField: "branch_name", subtitleField: "id", fields: const ["branch_name"]),
              GenericCrudScreen(title: "Attendance", endpoint: "attendance", titleField: "status", subtitleField: "attendance_date", fields: const ["employee", "attendance_date", "check_in", "check_out", "status"]),
              GenericCrudScreen(title: "Leaves", endpoint: "leaves", titleField: "leave_type", subtitleField: "status", fields: const ["employee", "leave_type", "start_date", "end_date", "status"]),
            ]),
          )
        ],
      ),
    );
  }
}

class PerformanceTab extends StatelessWidget {
  const PerformanceTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Column(
        children: [
          const TabBar(labelColor: Colors.black, tabs: [Tab(text: "Reviews"), Tab(text: "Promotions"), Tab(text: "History")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Reviews", endpoint: "performance", titleField: "score", subtitleField: "review_date", fields: const ["employee", "review_date", "score", "notes"]),
              GenericCrudScreen(title: "Promotions", endpoint: "promotions", titleField: "new_job_title", subtitleField: "old_job_title", fields: const ["employee", "promotion_date", "old_job_title", "new_job_title", "notes"]),
              GenericCrudScreen(title: "History", endpoint: "history", titleField: "field_changed", subtitleField: "change_date", fields: const ["employee", "field_changed", "old_value", "new_value"]),
            ]),
          )
        ],
      ),
    );
  }
}

class TrainingTab extends StatelessWidget {
  const TrainingTab({super.key});
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 4,
      child: Column(
        children: [
          const TabBar(isScrollable: true, labelColor: Colors.black, tabs: [Tab(text: "Programs"), Tab(text: "Records"), Tab(text: "Payroll"), Tab(text: "Bank")]),
          Expanded(
            child: TabBarView(children: [
              GenericCrudScreen(title: "Programs", endpoint: "training-programs", titleField: "program_name", subtitleField: "provider", fields: const ["program_name", "provider", "duration_days"]),
              GenericCrudScreen(title: "Records", endpoint: "training-records", titleField: "status", subtitleField: "enroll_date", fields: const ["employee", "training_program", "enroll_date", "status"]),
              GenericCrudScreen(title: "Payroll", endpoint: "payroll", titleField: "base_salary", subtitleField: "salary_type", fields: const ["employee", "salary_type", "base_salary", "pay_grade"]),
              GenericCrudScreen(title: "Bank", endpoint: "bank", titleField: "bank_name", subtitleField: "account_number", fields: const ["employee", "bank_name", "account_number", "iban"]),
            ]),
          )
        ],
      ),
    );
  }
}

// --- PLACEHOLDERS ---

class DashboardPlaceholder extends StatelessWidget {
  final String title;
  const DashboardPlaceholder({super.key, required this.title});
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Icon(Icons.dashboard, size: 80, color: Colors.teal),
          const SizedBox(height: 10),
          Text(title, style: const TextStyle(fontSize: 20)),
        ],
      ),
    );
  }
}

class PlaceholderApp extends StatelessWidget {
  final String title;
  const PlaceholderApp({super.key, required this.title});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Icon(Icons.build_circle, size: 80, color: Colors.grey),
          const SizedBox(height: 20),
          Text("$title\nComing Soon", textAlign: TextAlign.center, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.grey)),
        ],
      ),
    );
  }
}