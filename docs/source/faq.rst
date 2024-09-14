
FAQ
=======================================



.. _faq_soc:

「gpiozero」が動作しない場合。
-----------------------------------------------------------------------

Raspberry Pi 5 GPIO Python チュートリアルは gpiozero ライブラリに基づいており、設計プロセス中に徹底的にテストされています。

ただし、Raspberry Pi OS [1] 上の Linux カーネルの最近の変更により、GPIO システム コールの処理方法が変更され、元の Python ライブラリが Raspberry Pi 5 上の GPIO にアクセスできなくなりました。

当社の開発者はこの問題を gpiozero ライブラリに報告しており、gpiozero 開発者はこの問題を認識しており、更新に積極的に取り組んでいます [2]。

* [1] https://github.com/raspberrypi/linux/pull/6144
* [2] https://github.com/gpiozero/gpiozero/issues/1166

その間、
一時的な解決策を見つけました。以下のコマンドを実行すると、GPIO は正常に機能します。

.. code-block::

    sudo ln -s gpiochip0 /dev/gpiochip4

この解決策は、gpiozero ライブラリが適切な修正をリリースするまで有効です。