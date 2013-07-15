# 基本設計

## 2013.07.15
```
.
|-- README.md
|-- _labo
|   |-- mongo
|   |   |-- minimum.py
|   |   `-- system -> ../../system
|   |-- name
|   |   |-- main.py
|   |   `-- system -> ../../system
|   `-- twitter
|       |-- minimum.py
|       `-- system -> ../../system
|-- app.py
|-- asset
|   |-- __init__.py
|   |-- manager.py
|   |-- processor
|   |   |-- __init__.py
|   |   `-- serif
|   |       |-- __init__.py
|   |       `-- test.py
|   `-- resource
|       `-- serif
|           `-- test.json
|-- cli
|   `-- app.sh
|-- doc
|   |-- architecture.md
|   `-- src
|       `-- img
|           `-- hisyotan.jpg
|-- log
|   `-- 2013.0714.log
|-- skel
|   |-- __init__.py
|   |-- base.py
|   |-- filters.py
|   |-- interpreter.py
|   |-- procedure
|   |   |-- __init__.py
|   |   `-- test.py
|   `-- response
|       |-- __init__.py
|       `-- test.py
`-- system
    |-- __init__.py
    |-- conf.py
    |-- conf.sample.py
    |-- logger.py
    `-- util.py

21 directories, 28 files
```

## 2013.07.06.v2
```
.
|-- README.md
|-- System
|   |-- Config.py
|   |-- Logger.py
|   `-- __init__.py
|-- app.py
|-- asset
|   |-- __init__.py
|   `-- serif.py
|-- cli
|   `-- app.sh
|-- doc
|   |-- architecture.md
|   |-- docs.md
|   `-- src
|       |-- css
|       |-- img
|       |   `-- hisyotan.jpg
|       `-- js
|-- lib
|   |-- __init__.py
|   |-- twitter
|   |   |-- __init__.py
|   |   |-- bot.py
|   |   `-- oauth
|   |       `-- __init__.py
|   `-- util.py
|-- log
|-- skel
|   |-- __init__.py
|   |-- filter
|   |   `-- __init__.py
|   |-- interpreter
|   |   `-- __init__.py
|   |-- procedure
|   |   `-- __init__.py
|   `-- response
|       `-- __init__.py
`-- test
    `-- runner.sh

18 directories, 22 files
```

-------------
## 2013.07.06
- cli
    - app.sh コマンドラインからのパラメータを扱う
- app.py メインプロセスを提供する。skelから秘書たんを生成し、起動させる。
- skel 秘書たんの機能を定義する
    - skel.py 主にlib/twitterを操作する あと、この下のやつらを操作する領域
    - filter フィルタを定義する
        - retweet.py retweetかを判定する
    - interpret 発言を解釈し、次のProcessへのディスパッチと、パラメータの整形
        - interpret.py
    - process 発言毎に処理をする DBを扱える唯一の領域
        - task タスクカラムを操作する
        - person personレコードそのもののinsertやdeleteをする
        - remind リマインド関係のカラムを操作する
    - response 発言毎に返信を作る interpretとprocessの返り値を要求する
        - task
        - person
        - remind
- System
    - Conf.py
    -  Logger.py
- log/
- lib
    - twitter
        - instance.py インスタンスを生成して返すget(conf)のみをもつ。classの構造を定義する authenticate済み
        - oauth/ oauthを実装する領域
    - db
        - mongo
            - instance.py get(schema_name)のみをもつ。classの構造を定義する
