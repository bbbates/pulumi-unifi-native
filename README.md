# Unifi Pulumi Provider

A native Pulumi provider for managing Unifi resources.

## Goals

To:

- Provide a native Pulumi provider for Unifi resources, and
- Support all Unifi resources that can be managed via the Unifi API, and
- Be a good platform for which to build upon for more complex and common Unifi use cases

Currently, to manage Unifi resources via Pulumi, you need to make use of one of the Terraform providers, which are not complete.


## Status

- This provider is in very very early stages of development. I have the provider working with my reasonably simple Unifi ecosystem
(a Dream Machine, a few APs, a couple of switches, some basic firewall rules, and a few VLANs).

- Currently, I have only included the Python SDK, as that is what I am using. _If you would like to help out with the other SDKs, please let me know!_

- You will need to clone and build the provider to use locally. 

- Documentation is non-existent - this is a task for the future. Will be best to peruse the python SDK packages to get an understanding of what can be done with this provider.


## Build the provider 

```bash
$ make gen generate_schema provider install
```

This will:

1. Create the SDK codegen binary and place it in a `./bin` folder (gitignored)
2. Create the provider binary and place it in the `./bin` folder (gitignored)
4. Install the provider on your machine.


## Configuration

The following configuration options are available for the provider:

| Name                          | Description                                                               | Required | Default Value |
|-------------------------------|---------------------------------------------------------------------------|----------|---------------|
| `unifi-native:apiKey`         | The API key to use for authentication with the Unifi controller.          | Yes      |               |
| `unifi-native:apiHost`        | The hostname or IP address of the Unifi controller.                       | Yes      |               |
| `unifi-native:allowInsecure ` | If you are using a self-signed cert on the controller, set this to `true` | No       | `false`       |
| `unifi-native:siteId`         | The site name that the stack will be applied against                      | No       | `default`     |



### Importing Existing Resources

The type slugs generally follow the `unifi-native:lowercaseresourcename:CamelCaseResourceName. For example:

```bash
$ pulumi import 'unifi-native:firewallrule:FirewallRule' NameOfFirewallRule 'LONGID'
```


### Thanks to

- [Pulumi Provider Template](https://github.com/cloudy-sky-software/pulumi-provider-template) and @praneetloke
- [Unifi Community unifi-api project](https://github.com/ubiquiti-community/unifi-api/) - the openapi spec was generated from this project