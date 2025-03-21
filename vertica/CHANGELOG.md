# CHANGELOG - Vertica

<!-- towncrier release notes start -->

## 6.1.0 / 2025-01-16 / Agent 7.63.0

***Added***:

* Add `tls_ciphers` param to integration ([#19334](https://github.com/DataDog/integrations-core/pull/19334))

## 6.0.0 / 2024-10-04 / Agent 7.59.0

***Removed***:

* Remove support for Python 2. ([#18580](https://github.com/DataDog/integrations-core/pull/18580))

***Fixed***:

* Bump the version of datadog-checks-base to 37.0.0 ([#18617](https://github.com/DataDog/integrations-core/pull/18617))

## 5.0.0 / 2024-10-01 / Agent 7.58.0

***Changed***:

* Bump minimum version of base check ([#18733](https://github.com/DataDog/integrations-core/pull/18733))

***Added***:

* Bump the python version from 3.11 to 3.12 ([#18212](https://github.com/DataDog/integrations-core/pull/18212))

## 4.6.0 / 2024-08-09 / Agent 7.57.0

***Added***:

* Update dependencies ([#18187](https://github.com/DataDog/integrations-core/pull/18187))

## 4.5.0 / 2024-03-22 / Agent 7.53.0

***Added***:

* Update custom_queries configuration to support optional collection_interval ([#16957](https://github.com/DataDog/integrations-core/pull/16957))

***Fixed***:

* Document the `metric_prefix` option for custom queries ([#17061](https://github.com/DataDog/integrations-core/pull/17061))
* Update the configuration to include the `metric_prefix` option ([#17065](https://github.com/DataDog/integrations-core/pull/17065))

## 4.4.0 / 2024-01-05 / Agent 7.51.0

***Added***:

* Bump the Python version from py3.9 to py3.11 ([#15997](https://github.com/DataDog/integrations-core/pull/15997))
* Update dependencies ([#16394](https://github.com/DataDog/integrations-core/pull/16394)), ([#16502](https://github.com/DataDog/integrations-core/pull/16502))

## 4.3.0 / 2023-11-10 / Agent 7.50.0

***Added***:

* Updated dependencies. ([#16154](https://github.com/DataDog/integrations-core/pull/16154))

## 4.2.0 / 2023-09-29 / Agent 7.49.0

***Added***:

* Update Vertica dependency to 1.3.5 ([#15922](https://github.com/DataDog/integrations-core/pull/15922))

## 4.1.0 / 2023-08-18 / Agent 7.48.0

***Added***:

* Update dependencies for Agent 7.48 ([#15585](https://github.com/DataDog/integrations-core/pull/15585))

## 4.0.0 / 2023-08-10

***Changed***:

* Bump the minimum base check version ([#15427](https://github.com/DataDog/integrations-core/pull/15427))

***Added***:

* Update generated config models ([#15212](https://github.com/DataDog/integrations-core/pull/15212))

***Fixed***:

* Close and recreate a connection instead of using the `reset_connection` method ([#15413](https://github.com/DataDog/integrations-core/pull/15413))
* Fix types for generated config models ([#15334](https://github.com/DataDog/integrations-core/pull/15334))

## 3.5.0 / 2023-07-10 / Agent 7.47.0

***Added***:

* Bump dependencies for Agent 7.47 ([#15145](https://github.com/DataDog/integrations-core/pull/15145))

***Fixed***:

* Bump Python version from py3.8 to py3.9 ([#14701](https://github.com/DataDog/integrations-core/pull/14701))

## 3.4.1 / 2022-08-05 / Agent 7.39.0

***Fixed***:

* Dependency updates ([#12653](https://github.com/DataDog/integrations-core/pull/12653))

## 3.4.0 / 2022-08-03

***Added***:

* Use QueryManager to get metrics from queries ([#12542](https://github.com/DataDog/integrations-core/pull/12542))

## 3.3.2 / 2022-07-19

***Fixed***:

* Support projection storage and storage containers for Vertica 11+ ([#12465](https://github.com/DataDog/integrations-core/pull/12465))
* Make integration compatible with Vertica 11 ([#12394](https://github.com/DataDog/integrations-core/pull/12394))

## 3.3.1 / 2022-05-15 / Agent 7.37.0

***Fixed***:

* Upgrade dependencies ([#11958](https://github.com/DataDog/integrations-core/pull/11958))

## 3.3.0 / 2022-04-05 / Agent 7.36.0

***Added***:

* Upgrade dependencies ([#11726](https://github.com/DataDog/integrations-core/pull/11726))
* Add metric_patterns options to filter all metric submission by a list of regexes ([#11695](https://github.com/DataDog/integrations-core/pull/11695))

## 3.2.0 / 2022-02-19 / Agent 7.35.0

***Added***:

* Add `pyproject.toml` file ([#11454](https://github.com/DataDog/integrations-core/pull/11454))

***Fixed***:

* Fix namespace packaging on Python 2 ([#11532](https://github.com/DataDog/integrations-core/pull/11532))
* Remove unused `metric_prefix` in init_config ([#11464](https://github.com/DataDog/integrations-core/pull/11464))

## 3.1.1 / 2022-01-08 / Agent 7.34.0

***Fixed***:

* Add comment to autogenerated model files ([#10945](https://github.com/DataDog/integrations-core/pull/10945))

## 3.1.0 / 2021-10-04 / Agent 7.32.0

***Added***:

* Sync configs with new option and bump base requirement ([#10315](https://github.com/DataDog/integrations-core/pull/10315))
* Disable generic tags ([#10027](https://github.com/DataDog/integrations-core/pull/10027))

## 3.0.0 / 2021-08-22 / Agent 7.31.0

***Changed***:

* Remove messages for integrations for OK service checks ([#9888](https://github.com/DataDog/integrations-core/pull/9888))

## 2.1.1 / 2021-06-07 / Agent 7.29.0

***Fixed***:

* Fix required values in vertica ([#9479](https://github.com/DataDog/integrations-core/pull/9479))

## 2.1.0 / 2021-05-28

***Added***:

* Add runtime configuration validation ([#9003](https://github.com/DataDog/integrations-core/pull/9003))

## 2.0.2 / 2021-04-19 / Agent 7.28.0

***Fixed***:

* Fix logs section in example config file ([#8876](https://github.com/DataDog/integrations-core/pull/8876))

## 2.0.1 / 2021-03-07 / Agent 7.27.0

***Fixed***:

* Bump minimum base package version ([#8443](https://github.com/DataDog/integrations-core/pull/8443))

## 2.0.0 / 2021-01-25 / Agent 7.26.0

***Changed***:

* Update Vertica TLS implementation with in-house TLS library ([#8228](https://github.com/DataDog/integrations-core/pull/8228))

***Added***:

* Update Vertica to use use_tls config ([#8250](https://github.com/DataDog/integrations-core/pull/8250))

***Fixed***:

* Correct default template usage ([#8233](https://github.com/DataDog/integrations-core/pull/8233))

## 1.9.0 / 2020-12-11 / Agent 7.25.0

***Added***:

* Add option to limit metric collection ([#7997](https://github.com/DataDog/integrations-core/pull/7997))

## 1.8.0 / 2020-10-31 / Agent 7.24.0

***Added***:

* [doc] Add encoding in log config sample ([#7708](https://github.com/DataDog/integrations-core/pull/7708))

## 1.7.0 / 2020-09-21 / Agent 7.23.0

***Added***:

* Add config spec for Vertica ([#7513](https://github.com/DataDog/integrations-core/pull/7513))

***Fixed***:

* Use database config template in existing specs ([#7548](https://github.com/DataDog/integrations-core/pull/7548))

## 1.6.0 / 2020-08-10 / Agent 7.22.0

***Added***:

* Improve collection of library logs for debug flares ([#7252](https://github.com/DataDog/integrations-core/pull/7252))

***Fixed***:

* Use DEBUG log level for Vertica when Agent log level is DEBUG or TRACE ([#7264](https://github.com/DataDog/integrations-core/pull/7264))

## 1.5.0 / 2020-05-17 / Agent 7.20.0

***Added***:

* Allow optional dependency installation for all checks ([#6589](https://github.com/DataDog/integrations-core/pull/6589))
* Add version metadata ([#6346](https://github.com/DataDog/integrations-core/pull/6346))

## 1.4.1 / 2020-04-04 / Agent 7.19.0

***Fixed***:

* Remove logs sourcecategory ([#6121](https://github.com/DataDog/integrations-core/pull/6121))

## 1.4.0 / 2020-01-13 / Agent 7.17.0

***Added***:

* Use lazy logging format ([#5377](https://github.com/DataDog/integrations-core/pull/5377))

***Fixed***:

* Upgrade vertica to stop logging to /dev/null ([#5352](https://github.com/DataDog/integrations-core/pull/5352))

## 1.3.1 / 2019-11-14 / Agent 7.16.0

***Fixed***:

* Fix client log ([#5011](https://github.com/DataDog/integrations-core/pull/5011))

## 1.3.0 / 2019-11-14

***Added***:

* Add vertica lib log config ([#5005](https://github.com/DataDog/integrations-core/pull/5005))

## 1.2.0 / 2019-11-11

***Added***:

* Create a new connection at every check run when necessary ([#4983](https://github.com/DataDog/integrations-core/pull/4983))

## 1.1.1 / 2019-11-06

***Fixed***:

* Recreate connection when closed ([#4958](https://github.com/DataDog/integrations-core/pull/4958))

## 1.1.0 / 2019-10-11 / Agent 6.15.0

***Added***:

* Add more Vertica metrics ([#4649](https://github.com/DataDog/integrations-core/pull/4649))

## 1.0.0 / 2019-08-24 / Agent 6.14.0

***Added***:

* Add Vertica integration ([#3890](https://github.com/DataDog/integrations-core/pull/3890))
