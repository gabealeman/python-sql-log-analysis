# Python SQL Log Analysis

## Introduction

> Using Python 2.7 to connect to a database, and use SQL queries to analyze the log data, and print out the answers to some questions.



## Installation

>Install VirtualBox
>Install Vagrant
>Download the VM configuration
- https://github.com/udacity/fullstack-nanodegree-vm
>Download SQL Log File
- https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
>Extract newsdata.sql into vagrant directory of VM configuration's
>Using terminal CD to VM configuration vagrant directory and run
- `vagrant up`
- `vagrant ssh`
- `cd /vagrant`
- `psql -d news -f newsdata.sql`
> Move log-analysis.py to your vagrant directory
- And run `python log-analysis.py`
