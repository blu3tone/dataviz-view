# Dashboard Demo

This repository is used to store resource code of Dashboard Demo

## Getting Started

These instructions will get you install and run application on local computer

### Prerequisites

What things you need to install the software and how to install them

```
NodeJs
```

### Installing

A step by step series of examples that tell you have to get a development env running

- Open git bash or Windows Poweshell console 

```
(Windows + x + A)
```

- Go to application directory

```
cd 'C:\...\dataviz-view\DashboardDemo'
```

- Install bower by following command

```
npm install -g bower
```

- Install bower packages


```
bower install
```

- Go to application directory

```
cd 'C:\...\dataviz-view\DashboardDemo'
```

## Deployment

There are 2 ways to run the application

### Run local files

By this way, just able to run application on Google Chrome

- Create shortcut of Google Chrome
- Open Properies
- add following console to the end of field Target

```
--allow-file-access-from-files
```

It will be look like

```
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --allow-file-access-from-files
```

After that, open index.html

### Run nodejs http server

- Install NodeJs and run following command by Windows Powershell

```
npm install -g http-server
```

- Access to resouce directory

```
cd 'C:\...\dataviz-view\DashboardDemo\app'
```

- Then run

```
http-server
```

Console will be like
```
Starting up http-server, serving ./
Available on:
  http://192.168.0.5:8080
  http://127.0.0.1:8080
Hit CTRL-C to stop the server
```
After that, u can open url http://127.0.0.1:8080 to lunch application

## Built With

* [AngularJS](http://angularjs.org) - The web framework used
* [Bootstrap](http://getbootstrap.com) - UI library
* to be defining

## Contributing

* to be defining

## Versioning

* to be defining

## Authors

* **Long Tran Vu** - *Initial work* - [PurpleBooth](https://github.com/Dr4g0nH3r0)

## License

* Has not defined yet


