# Description

nagios-plugins-fts provides a set of nagios plugins to monitor both status
and performance of FTS servers.

## Probes details

3 Nagios probes have been implemented

* check_fts_service: to check if the FTS REST Service is up and running
* check_fts_stalled_server: to check if the FTS server is stalled and it's not properly processing transfers
* check_fts_stalled_transfers: to check if there are stuck transfers in the cluster

Example of host and service definitions are  provided under the 'config' folder. 

In particular the check_fts_service and check_fts_stalled_server probes need to run for each nodes part of the FTS cluster,
while the check_fts_stalled_transfers probe is supposed to run once for the whole cluster (e.g. contacting the FTS alias).

# Contact

Send and email to fts-support@cern.ch if you have questions
regarding the use of this software. To submit patches or suggest improvements
send an email to fts-devel@cern.ch

# Authors

CERN File Transfer Service (FTS) Team <fts-devel@cern.ch>

# License

Copyright 2013 the European Middleware Initiative
Copyright 2014-2016 CERN

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
