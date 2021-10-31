### Export Dashboard


While Dashboard is open, click "Share" icon on top of the page and
select "Export" tab to save it to a JSON file.


### Import Dashboard


While on Dashboard home page, click "Home" menu on the left top corner
and select "Import dashboard" option to upload a JSON file.


### Export Data Sources


Run command below in terminal.


``` {.prettyprint .linenums .lang-rb}
$ curl -s "http://www.your-host.com/datasources" -u admin:grafana|jq -c -M '.[]'|split -l 1 - path/to/export/datasource/
```


### Restore Data Sources


Run command below in terminal.


``` {.prettyprint .linenums .lang-rb}
$ for i in path/to/export/datasource/*; do \    curl -X "POST" "http://www.your-host.com/datasources" \    -H "Content-Type: application/json" \    --user admin:grafana \    --data-binary @$idone
```
