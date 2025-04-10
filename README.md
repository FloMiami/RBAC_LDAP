# RBAC LDAP Integration Project

This project demonstrates the implementation of Identity and Access Management (IAM) within a VMware virtual network using OpenLDAP for user management and Role-Based Access Control (RBAC). It showcases how to define an LDAP directory structure, create users, groups, and roles, and assign permissions. A simple server-client application is included to illustrate the enforcement of these access controls.

**Key Features:**

* **OpenLDAP Implementation:** Utilizes OpenLDAP for centralized user and group management.
* **Role-Based Access Control (RBAC):** Defines roles with specific permissions and assigns them to users and groups for controlled access.
* **LDAP Directory Structure:** Configured with organizational units (OUs) for People, Groups, and Roles, as defined in the `ldap_config` directory.
* **Server-Client Application:** A basic Python application located in the `employee_directory` that relies on the LDAP setup for authentication and authorization.
* **LDIF Configuration:** The `ldap_config` directory contains LDIF files (`base_structure.ldif`, `users.ldif`, `groups.ldif`, `roles.ldif`, `assign_role.ldif`) defining the LDAP directory structure and initial data.

**Setup:**

To run this project in your own environment, you will need to:

1.  **Set up a virtual network environment (e.g., using VMware) with at least two virtual machines.** One VM will host the LDAP server, and the other will run the server-client application.
2.  **Install and configure OpenLDAP on the designated LDAP server VM.** You will need to apply the LDIF configurations provided in the `ldap_config` directory to initialize your LDAP database.
3.  **Configure network settings to allow communication between the VMs.**
4.  **Install the necessary dependencies for the server-client application** as listed in `employee_directory/requirements.txt`.
5.  **Important:** The server-client application (specifically within `employee_directory/app/__init__.py`) previously contained a secret key. **This key has been revoked for security reasons.** You will need to generate and set your own unique secret key within the application's configuration to run it properly.
6.  **Update IP Address:** This project was developed using a specific local IP address for the LDAP server: `192.168.175.128`. You will need to **replace this placeholder IP address** in any relevant configuration files within the server-client application to match the actual IP address of your LDAP server VM in your local environment.

**Directory Structure:**

.
├── employee_directory/
│   ├── app/
│   │   ├── auth.py
│   │   ├── init.py
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── directory.html
│   │   │   └── login.html
│   │   └── views.py
│   ├── requirements.txt
│   └── run.py
├── ldap_config/
│   ├── assign_role.ldif
│   ├── base_structure.ldif
│   ├── groups.ldif
│   ├── myenv/         # (Likely a virtual environment - can be ignored)
│   ├── requirements.txt
│   ├── roles.ldif
│   └── users.ldif
└── README.md

**Demonstration:**

The `employee_directory` application provides a basic interface to demonstrate how the LDAP-managed users and roles control access. Once set up, you should be able to:

* Authenticate users against the OpenLDAP server.
* See different levels of access or information based on the roles assigned to the logged-in user.

This project provides a practical example of implementing IAM principles in a virtualized environment.
