import os
import sys

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QCheckBox, QListWidgetItem

from MainUI import Ui_DoCST
from Calculation3D import Calculation3D


class MainUI(Ui_DoCST, QMainWindow):
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)
        self.registerEvent()

        self.freq_lineEdit.setText("1.0")
        self.ind_lineEdit.setText("1.0")
        self.cap_lineEdit.setText("1.0")

        self.main_coupling = {}
        self.cross_coupling = {}
        self.sl_coupling = {}
        self.freq_data = {}
        self.extra_coupling = {}

        self.ideal_main_coupling = {}
        self.ideal_cross_coupling = {}
        self.ideal_sl_coupling = {}
        self.ideal_freq_data = {}
        self.ideal_coupling = {}

        self.freq_change = []
        self.coupling_change = []
        self.freq_change_value = {}
        self.coupling_change_value = {}

        self.negative_index = []
        self.is_negative_list_update = True

        self.is_extra_update = False
        self.is_ideal_update = False

        # self.model = QStandardItemModel()
        # self.item = []

    def registerEvent(self):
        """通信事件注册"""
        self.apply_btn.clicked.connect(self.apply_click)
        self.coupling_plainTextEdit.textChanged.connect(self.update_extra_text)
        self.ideal_plainTextEdit.textChanged.connect(self.update_ideal_text)
        self.load_btn.clicked.connect(self.load_click)
        self.save_btn.clicked.connect(self.save_click)

    @staticmethod
    def apply_click():
        """‘Apply’按钮点击事件"""
        """获取斜率信息"""
        _freq = float(main.freq_lineEdit.text())
        _cap = float(main.cap_lineEdit.text())
        _ind = float(main.ind_lineEdit.text())
        """设置斜率信息"""
        _calculation = Calculation3D(freq_coefficient=_freq, cap_coefficient=_cap, ind_coefficient=_ind)
        """如果数据有更新，则更新计算值"""
        if main.is_ideal_update or main.is_extra_update:
            """计算频率变化值"""
            main.freq_change = _calculation.cal_freq(freq_extra=main.freq_data.values(),
                                                     freq_ideal=main.ideal_freq_data.values())
            """enumerate()函数可获得迭代器元素的索引值"""
            if main.freq_change:
                """将频率变化值与对应频率绑定"""
                for index, x in enumerate(main.freq_data.keys()):
                    main.freq_change_value[x] = main.freq_change[index]
                """显示频率计算值"""
                main.display_freq()
                """清空频率变化值数据，等待下一次更新"""
                main.freq_change_value.clear()
            else:
                main.freq_textBrowser.setText('频率数据错误！')

        """将交叉耦合和主耦合合并为一个字典"""
        main.extra_coupling = dict(main.main_coupling, **main.cross_coupling)
        main.ideal_coupling = dict(main.ideal_main_coupling, **main.ideal_cross_coupling)
        """计算耦合变化值"""
        main.coupling_change = _calculation.cal_coupling(negative_index=main.get_negative_item(),
                                                         coupling_extra=main.extra_coupling.values(),
                                                         coupling_ideal=main.ideal_coupling.values())

        if main.coupling_change:
            for index, x in enumerate(main.ideal_coupling.keys()):
                main.coupling_change_value[x] = main.coupling_change[index]
            main.display_coupling()
            main.coupling_change_value.clear()
        else:
            main.coupling_textBrowser.setText('耦合数据错误！')

    def display_coupling(self):
        """显示耦合变化值"""
        text_view = '\n'.join([str(x) for x in self.coupling_change_value.items()])
        self.coupling_textBrowser.setText(text_view)

    def display_freq(self):
        """显示频率变化值"""
        text_view = '\n'.join([str(x) for x in self.freq_change_value.items()])
        self.freq_textBrowser.setText(text_view)

    def get_negative_item(self):
        """获取负耦合序数"""
        negative_index = []
        negative_item = [self.negative_list.itemWidget(self.negative_list.item(i))
                         for i in range(self.negative_list.count())]
        for _i, i in enumerate(negative_item):
            if i.isChecked():
                negative_index.append(_i)
        return negative_index

    def load_click(self):
        """'Load'按钮点击事件"""
        main_data = []
        set_data = []
        fileName, fileType = QFileDialog.getOpenFileName(self, "Choose File", os.getcwd(),
                                                         "All Files(*);;Text Files(*.txt);;S2P Files(*.s2p)")
        if fileName == "":
            return
        else:
            with open(fileName) as file_object:
                file_contents = file_object.read()
                for i in range(len(file_contents.split('\n')) - 3):
                    main_data.append(file_contents.split('\n')[i])
                main_data_str = '\n'.join([str(x) for x in main_data])
                self.ideal_plainTextEdit.setPlainText(main_data_str)

                for i in range(3):
                    for index, _i in enumerate(file_contents.split('\n')
                                               [len(file_contents.split('\n')) - 3 + i].split()):
                        if index == 2:
                            set_data.append(_i)
                self.freq_lineEdit.setText(set_data[0])
                self.ind_lineEdit.setText(set_data[1])
                self.cap_lineEdit.setText(set_data[2])

    def save_click(self):
        """'Save'按钮点击事件"""
        data_to_save = (self.ideal_plainTextEdit.toPlainText() + '\n' + 'freq = ' + self.freq_lineEdit.text() +
                        '\n' + 'ind = ' + self.ind_lineEdit.text() + '\n' + 'cap = ' + self.cap_lineEdit.text())
        fileName, fileType = QFileDialog.getSaveFileName(self, "Save File", os.getcwd(),
                                                         "All Files(*);;Text Files(*.txt);;S2P Files(*.s2p)")
        if fileName == "":
            return
        else:
            with open(fileName, 'w') as file_object:
                file_object.write(data_to_save)

    def update_extra_text(self):
        self.is_extra_update = True
        """清空提取值数据"""
        self.main_coupling.clear()
        self.cross_coupling.clear()
        self.freq_data.clear()
        self.sl_coupling.clear()
        """填充提取值数据"""
        main.set_coupling_data(_text=self.coupling_plainTextEdit.toPlainText().split('\n'),
                               _cross_coupling_dict=self.cross_coupling, _freq_data_dict=self.freq_data,
                               _main_coupling_dict=self.main_coupling, _sl_coupling_dict=self.sl_coupling)

    def update_ideal_text(self):
        self.is_ideal_update = True
        """判断理想值是否更新"""
        old_keys = dict(self.ideal_main_coupling, **self.ideal_cross_coupling).keys()
        """清空理想值数据"""
        self.ideal_main_coupling.clear()
        self.ideal_cross_coupling.clear()
        self.ideal_freq_data.clear()
        self.ideal_sl_coupling.clear()
        """填充理想值数据"""
        main.set_coupling_data(_text=self.ideal_plainTextEdit.toPlainText().split('\n'),
                               _cross_coupling_dict=self.ideal_cross_coupling, _freq_data_dict=self.ideal_freq_data,
                               _main_coupling_dict=self.ideal_main_coupling, _sl_coupling_dict=self.ideal_sl_coupling)
        """如果拓扑更新，更新相应耦合复选框"""
        if old_keys != dict(self.ideal_main_coupling, **self.ideal_cross_coupling).keys():
            self.negative_list.clear()
            self.set_negative_list()
        """如果拓扑未更新，则耦合复选框保持不变"""
        if self.is_negative_list_update:
            self.set_negative_list()

    def set_negative_list(self):
        """设置多选框-用listview实现"""
        # self.item.clear()
        # self.model.clear()
        # for _i, i in enumerate(dict(self.main_coupling, **self.cross_coupling).keys()):
        #     self.item.append(QStandardItem(i))
        #     self.item[_i].setCheckable(True)
        #     self.model.appendRow(self.item[_i])
        #     self.negative_listView.setModel(self.model)
        """设置多选框-用listwidget实现"""
        for _i, i in enumerate(dict(self.ideal_main_coupling, **self.ideal_cross_coupling).keys()):
            _box = QCheckBox(i)
            _item = QListWidgetItem()
            self.negative_list.addItem(_item)
            self.negative_list.setItemWidget(_item, _box)
        """标记取反"""
        self.is_negative_list_update = False

    def get_coefficient(self):
        """获取默认斜率参数"""
        return self.freq_lineEdit.text(), self.cap_lineEdit.text(), self.ind_lineEdit.text()

    @staticmethod
    def set_coupling_data(*, _text, _freq_data_dict, _cross_coupling_dict, _main_coupling_dict,
                          _sl_coupling_dict):
        for text in _text:
            if text.startswith('f'):
                _freq_data_dict[text.split()[0]] = text.split()[2]
            elif text.startswith('CBW'):
                re_text = text.replace(',', '', 1).split()
                if re_text[0].startswith('CBWS') or re_text[0].endswith('L'):
                    _sl_coupling_dict[re_text[0]] = re_text[2]
                else:
                    if int(re_text[0][4:]) - int(re_text[0][3]) == 1:
                        _main_coupling_dict[re_text[0]] = re_text[2]
                    else:
                        _cross_coupling_dict[re_text[0]] = re_text[2]
            else:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())
