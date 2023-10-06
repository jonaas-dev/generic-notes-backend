<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Php](#php)
  - [Libraries & others](#libraries--others)
  - [PHP CS FIXER](#php-cs-fixer)
  - [PHP CODE SNIFFER](#php-code-sniffer)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Php
<!-- --------------------------------------------- -->

## Libraries & others

- [PhpSpreadsheet](https://github.com/PHPOffice/PhpSpreadsheet): Print pdfs.
- [Graph](https://github.com/graphp/graph) - Data Structure
- [RoboTask](https://github.com/consolidation/robo) Modern and simple PHP task runner inspired by Gulp, Tasks:
  - writing cross-platform scripts
  - processing assets (less, sass, minification)
  - running tests
  - executing daemons (and workers)
  - watching filesystem changes
  - deployment with sftp/ssh/docker
  
## PHP CS FIXER

Font: https://github.com/PHP-CS-Fixer/PHP-CS-Fixer

```bash
composer require friendsofphp/php-cs-fixer --dev
# Note: in windows 10 not working because the run file need .bat 
```

```bash
# For windows
composer global require "friendsofphp/php-cs-fixer=*"
```

How to configure in PhpStorm?

- `ALT` + `CTRL` + `S` => 'php'
- Add php-cs-fix path

How to obtain path?

```bash
where.exe php-cs-fixer 
# C:\Users\manolo\AppData\Roaming\Composer\vendor\bin\php-cs-fixer
# C:\Users\manolo\AppData\Roaming\Composer\vendor\bin\php-cs-fixer.bat <------ :)
```

:warning: m'he acabat barallant molt amb php i no he acabat aconseguint res. Tinc un document `.php-cs-fixer.php``on hi han algunes configuracions pero tinc problemes amb:

- el script del composer no li puc passar el "document actual", no vull anar hardcodejant.
- el exclude() no em funciona

Una solució temporal que he trobat és configurar un `File watcher` (adjunto imatge).

![image](https://user-images.githubusercontent.com/100514206/221419246-2f59829e-24a7-44f5-8245-547bef098023.png)

## PHP CODE SNIFFER

Font: https://github.com/squizlabs/PHP_CodeSniffer

```bash
composer require "squizlabs/php_codesniffer": "3.*" --dev
```

How to configure in PhpStorm?

- `ALT` + `CTRL` + `S` => 'php'
- Add php-codesniffer path

:warning: M'he sortit amb la meva pero penso que si no miro d'unificar els standards que tinc en el PHP CS FIXER i els que tinc amb el PHP CODE SNIFFER, no anirem bé.

Tinc les configuracions en el document `phpcs.xml.dist`. He estat fent proves i es porta força bé.
