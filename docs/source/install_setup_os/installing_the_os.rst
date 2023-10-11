.. _install_os:

OSのインストール（一般手順）
========================================

**ステップ1**

Raspberry Piは、Mac OS、Ubuntu 18.04、およびWindowsで動作するグラフィカルなSDカード書き込みツールを開発しています。このツールはほとんどのユーザーにとって最も簡単な選択肢であり、イメージを自動的にダウンロードしてSDカードにインストールします。

ダウンロードページ（https://www.raspberrypi.org/software/）にアクセスし、お使いのOSに対応した **Raspberry Pi Imager** のリンクをクリックします。ダウンロードが完了したら、インストーラーを起動します。

.. image:: img/image11.png
    :align: center

**ステップ2**

インストーラーを起動すると、OSが実行をブロックしようとする場合があります。例えば、Windowsでは以下のようなメッセージが表示されます：

このようなポップアップが表示された場合は、 **More info** をクリックしてから **Run anyway** をクリックし、Raspberry Pi Imagerのインストール手順に従います。

.. image:: img/image12.png
    :align: center

**ステップ3**

SDカードをコンピューターまたはラップトップのSDカードスロットに挿入します。

**ステップ4**

Raspberry Pi Imager内で、インストールしたいOSと使用するSDカードを選択します。

.. image:: img/image13.png
    :align: center

.. note::

    * 初回はインターネットに接続している必要があります。
    * 選択したOSは、今後オフラインで使用するために保存されます（ ``lastdownload.cache`` 、 ``C:/Users/yourname/AppData/Local/Raspberry Pi/Imager/cache`` ）。次回ソフトウェアを起動する際、コンピューターにキャッシュされた日付が表示されます。

.. Download the `raspios_armhf-2020-05-28 <https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip>`_ image and select it in Raspberry Pi Imager.

.. .. image:: img/otherOS.png
..     :align: center

.. .. warning::
..     Raspberry Pi OS has major changes after the 2021-05-28 version, which may cause some functions to be unavailable. Please do not use the latest version for now.


.. .. mark

**ステップ5**

使用するSDカードを選択します。

.. image:: img/image14.png
    :align: center

**ステップ6**

**Ctrl+Shift+X** を押すか、 **setting** アイコンをクリックして **Advanced options** ページを開き、SSHを有効にし、ユーザー名とパスワードを設定します。

    .. note::
        * Raspberry Piにはデフォルトのパスワードがないため、自分で設定する必要があります。また、ユーザー名も変更できます。
        * リモートアクセスの場合、SSHも手動で有効にする必要があります。

.. image:: img/image15.png
    :align: center

その後、Wi-Fi設定を完了し、 **SAVE** をクリックします。

.. note::

    ``wifi country`` は、Raspberry Piを使用している国の2文字の `ISO/IEC alpha2コード  <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定する必要があります。

.. image:: img/image16.png
    :align: center

**ステップ7**

**WRITE** ボタンをクリックします。

.. image:: img/image17.png
    :align: center

**ステップ8**

SDカードに既存のファイルがある場合は、それらのファイルをバックアップしてから進めてください。バックアップするファイルがない場合は、 **Yes** をクリックします。

.. image:: img/image18.png
    :align: center

**ステップ9**

一定時間待った後、書き込みが完了したことを示すウィンドウが表示されます。

.. image:: img/image19.png
    :align: center

