# Setup  
### (一)安裝及設定  
1. 安裝R, 並將目錄加入環境變數path中  *note:預設:C:\Program Files\R\R-3.6.1*  
1. [根據python版本下載rpy2.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2)  
1. 設定變數R_USER, 值為使用者名稱  
1. pip install rpy2.whl    

### (二)安裝package 
1. 開啟R
1. 程式套件 -> Install packages from local files -> 選bcra.zip  
# Usage  
```php=
<?php
    $command = escapeshellcmd('path/to/BCRA_run.py ID T1 T2 N_Biop HypPlas AgeMen Age1st N_Rels Race');
    $output = shell_exec($command);
    echo $output;
?>
```
# Agruments
**ID**  
**T1** 填表人目前年齡  
**T2** 切片時的年齡  
**N_Biop** 乳房切片次數，unk=99  
**HypPlas** atypical=1,no=0,unk=99  
**AgeMen** 初經年齡, unk=99  
**Age1st** 第一次懷孕年齡, 未產=98 , unk=99  
**N_Rels** 一等親得乳癌數量. 父母兄弟姊妹, unk=99  
**Race** 1=白人, 11=華人  
