# Agent Check: Confluent Platform

## Overview

This check monitors Confluent Platform and Kafka components through the Datadog Agent.

This integration collects JMX metrics for the following components:

- Broker
- Connect
- Replicator
- Schema Registry
- ksqlDB Server
- Streams
- REST Proxy

Consider [Data Streams Monitoring][11] to enhance your Confluent Platform integration. This solution enables pipeline visualization and lag tracking, helping you identify and resolve bottlenecks.

## Setup


### Installation

The Confluent Platform check is included in the [Datadog Agent][1] package. No additional installation is needed on your Confluent Platform component server.

**Note**: This check collects metrics with JMX. A JVM is required on each node so the Agent can run [jmxfetch][2]. It is recommended to use an Oracle-provided JVM.


### Configuration

1. Edit the `confluent_platform.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to collect your Confluent Platform performance data. See the [sample confluent_platform.d/conf.yaml][3] for all available configuration options.

    For each component, you need to create a separate instance to collect its JMX metrics. The list of default metrics collected are listed in [`metrics.yaml` file][4], for example:

    ```yaml
    instances:
     - host: localhost
       port: 8686
       name: broker_instance
       user: username
       password: password
     - host: localhost
       port: 8687
       name: schema_registry_instance
     - host: localhost
       port: 8688
       name: rest_proxy_instance
    ```

2. [Restart the Agent][5].

##### Log collection

_Available for Agent versions >6.0_

1. Collecting logs is disabled by default in the Datadog Agent, you need to enable it in `datadog.yaml`:

   ```yaml
   logs_enabled: true
   ```

2. Add this configuration block to your `confluent_platform.d/conf.yaml` file to start collecting your Confluent Platform components logs:

   ```yaml
     logs:
       - type: file
         path: <CONFLUENT_COMPONENT_PATH>/logs/*.log
         source: confluent_platform
         service: <SERVICE_NAME>
         log_processing_rules:
           - type: multi_line
             name: new_log_start_with_date
             pattern: \[\d{4}\-\d{2}\-\d{2}
   ```

    Change the `path` and `service` parameter values and configure them for your environment. See the [sample confluent_platform.d/conf.yaml][3] for all available configuration options.

3. [Restart the Agent][6].

##### Metric collection

For containerized environments, see the [Autodiscovery with JMX][7] guide.

### Validation

[Run the Agent's status subcommand][8] and look for `confluent_platform` under the **JMXFetch** section.

```
    ========
    JMXFetch
    ========

      Initialized checks
      ==================
        confluent_platform
          instance_name : confluent_platform-localhost-31006
          message :
          metric_count : 26
          service_check_count : 0
          status : OK
```

## Data Collected

### Metrics

See [metadata.csv][6] for a list of metrics provided by this check.

### Events

The Confluent Platform check does not include any events.

### Service Checks

See [service_checks.json][9] for a list of service checks provided by this integration.

## Troubleshooting

Need help? Contact [Datadog support][10].


[1]: /account/settings/agent/latest
[2]: https://github.com/DataDog/jmxfetch
[3]: https://github.com/DataDog/integrations-core/blob/master/confluent_platform/datadog_checks/confluent_platform/data/conf.yaml.example
[4]: https://github.com/DataDog/integrations-core/blob/master/confluent_platform/datadog_checks/confluent_platform/data/metrics.yaml
[5]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[6]: https://github.com/DataDog/integrations-core/blob/master/confluent_platform/metadata.csv
[7]: https://docs.datadoghq.com/agent/guide/autodiscovery-with-jmx/?tab=containerizedagent
[8]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[9]: https://github.com/DataDog/integrations-core/blob/master/confluent_platform/assets/service_checks.json
[10]: https://docs.datadoghq.com/help/
[11]: https://docs.datadoghq.com/data_streams/
