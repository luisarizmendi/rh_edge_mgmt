# Ansible Collection - luisarizmendi.rh_edge_mgmt

This Ansible Collection helps installing and configuring the following architecture for demos and PoCs:

![demo-arch](docs/images/demo-arch.png)

## Roles

The collection is composed by two main roles:

* [config_rh_edge-mgmt-node](roles/setup_rh_edge-mgmt-node/README.md) that deploy RHDE management services

This Ansible Role was created to be used as a simple way of deploying all Management components that you would need to run a Red Hat Edge Management DEMO:

* Image Builder
* FDO Servers
* Ansible Automation Platform (Controller, Hub and Event Driven Automation)
* Gitea

* [setup_rh_edge-mgmt-node](roles/config_rh_edge-mgmt-node/README.md) that configure those services

This Ansible Role was created to be used as a simple way of configuring the following components that you would need to run a Red Hat Edge Management DEMO:

* Ansible Automation Platform (Controller and Event Driven Automation)
* Gitea

## Pre-requisites

### Ansible Collection

You need to install the [Ansible Collection](https://github.com/luisarizmendi/rh_edge_mgmt) on your laptop:

```shell
ansible-galaxy collection install luisarizmendi.rh_edge_mgmt
```

### Hardware requirements

I've been able to deploy everything on a VM with 4 vCores and 10GB of memory. Storage will depend on the number of RHDE images that you generate.

### Roles pre-requisites

This is the summary of the pre-requisites (all for installing the services):

* Ansible Automation Platform Manifest file
* Red Hat Customer Portal Offline Token
* Red Hat Pull Secret
* Red Hat User and Password

You can find more details about them in the role README file:

* [setup_rh_edge_mgmt_node role](https://github.com/luisarizmendi/rh_edge_mgmt/tree/main/roles/setup_rh_edge_mgmt_node)

You can also take a look at the pre-requistes of the config role, but mainly is demo config customization

* [config_rh_edge_mgmt_node role](https://github.com/luisarizmendi/rh_edge_mgmt/tree/main/roles/config_rh_edge_mgmt_node)

  >**Note**
  >
  > You can ignore the additional Collections installation since those should be installed as part of the `luisarizmendi.rh_edge_mgmt` collection install.



### Ansible inventory and playbook

Prepare the Ansible inventory file and the variables in the `main.yml` playbook as explained in the roles README files, for example:

```yaml
---
- name: RHDE and AAP Demo
  hosts:
    - edge_management
  tasks:
    - name: Install management node
      ansible.builtin.include_role:
        name: luisarizmendi.rh_edge_mgmt.setup_rh_edge_mgmt_node

    - name: Config management node
      ansible.builtin.include_role:
        name: luisarizmendi.rh_edge_mgmt.config_rh_edge_mgmt_node
      vars:
        gitea_admin_repos_template: ../templates/gitea_admin_repos
        gitea_user_repos_template: ../templates/gitea_user_repos
        aap_config_template: ../templates/aap_config.j2
        aap_repo_name: aap
```

Be sure that you include all secrets, preferably using an Ansible Vault file by adding `--ask-vault-pass` while launching the script:

```shell
ansible-playbook -vvi inventory --ask-vault-pass playbooks/main.yml
```


## Demo example

You have a base [demo example under docs/example](https://github.com/luisarizmendi/rh_edge_mgmt/tree/main/docs/example) that you can use as starting point.

