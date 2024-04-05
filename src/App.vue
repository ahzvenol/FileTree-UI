<template>
  <div>
    <div id="back" @click="back"></div>
    <!-- todo:路径输入跳转 -->
    <input type="text" readonly="readonly" v-model="path" />
    <div
      id="file"
      ref="file"
      @dragover="onDragOver()"
      @dragleave="restore()"
      @drop="
        onFileChange($event);
        restore();
      "
    >
      在此拖入文件
    </div>
    <tree :object="part" />
  </div>
</template>

<script>
import Tree from './components/Tree.vue';
export default {
  name: 'App',
  data() {
    return {
      path: '',
      part: {},
      history: [],
      preDic: {},
      // todo:提前计算出所有path:part的解决方案
    };
  },
  components: {
    Tree,
  },
  watch: {
    path() {
      this.history.push(this.path);
      this.part = this.preDic[this.path];
    },
  },
  methods: {
    back() {
      this.path = this.history[this.history.length - 1];
      this.history.pop();
    },
    onDragOver() {
      this.$refs.file.style.border = '2px dashed #64A4F2';
      this.$refs.file.style.color = '#64A4F2';
    },
    restore() {
      this.$refs.file.style.border = '2px dashed #dfdfdf';
      this.$refs.file.style.color = '#999999';
    },
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      let reader = new FileReader();
      reader.onload = evR => {
        let pre = (path, obj) => {
          this.preDic[path] = obj;
          try {
            for (let o of obj) {
              if (o['content']) {
                pre(path + o.info['fileName'] + '/', o['content']);
              }
            }
          } catch (e) {
            console.log(obj);
          }

        };
        pre('./', JSON.parse(this.removeExtComma(evR.target.result)));
        this.path = './';
      };
      reader.readAsText(files[0], 'UTF-8');
    },
    removeExtComma(str) {
      let i,
        j,
        len,
        list,
        c,
        notValue = null,
        preQuot = null,
        lineNum;
      list = String(str).split('');
      for (i = 0, len = list.length; i < len; i++) {
        c = list[i];
        //单引或双引
        if (/^[\'\"]$/.test(c)) {
          if (notValue === null && preQuot === null) {
            notValue = false;
            preQuot = i;
            continue;
          }
          //值
          if (!notValue) {
            //前面反斜杠个数
            lineNum = 0;
            for (j = i - 1; j > -1; j--) {
              if (list[j] === '\\') {
                lineNum++;
              } else {
                j = -1;
              }
            }
            //个数为偶数且和开始引号相同
            //结束引号
            if (lineNum % 2 === 0) {
              if (list[preQuot] === c) {
                notValue = true;
                preQuot = -1;
              }
            }
          }
          //非值
          else {
            //开始引号
            if (preQuot == -1) {
              preQuot = i;
              notValue = false;
            }
            //结束引号
            else if (list[preQuot] === c) {
              notValue = true;
              preQuot = -1;
            }
          }
        }
        //逗号
        else if (c === ']' || c === '}') {
          //非值
          if (notValue) {
            for (j = i - 1; j > -1; j--) {
              if (/^[\t\r\n\s ]+$/.test(list[j])) {
                continue;
              } else {
                if (list[j] === ',') list[j] = '';
                break;
              }
            }
          }
        }
      }
      return list.join('');
    },
  },
  beforeCreate() {
    Date.prototype.format = function (fmt) {
      let o = {
        'M+': this.getMonth() + 1, //月份
        'd+': this.getDate(), //日
        'h+': this.getHours(), //小时
        'm+': this.getMinutes(), //分
        's+': this.getSeconds(), //秒
        'q+': Math.floor((this.getMonth() + 3) / 3), //季度
        S: this.getMilliseconds(), //毫秒
      };
      if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + '').substr(4 - RegExp.$1.length));
      for (let k in o)
        if (new RegExp('(' + k + ')').test(fmt))
          fmt = fmt.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k] : ('00' + o[k]).substr(('' + o[k]).length));
      return fmt;
    };
  },
  mounted() {
    document.ondragover = function (event) {
      event.preventDefault();
    };
    document.ondrop = function (event) {
      event.preventDefault();
    };
  },
};
</script>

<style>
* {
  border: 0;
  padding: 0;
  margin: 0;
  user-select: none;
}

body {
  padding-left: 8px;
  /* 处理未知原因边界溢出 */
  overflow: hidden;
}

#back {
  width: 34px;
  height: 37px;
  /* 正值对整体结构有影响,使用负值校准位置 */
  margin-bottom: -14px;
  display: inline-block;
  background-image: url(./assets/back.png);
  background-blend-mode: lighten;
  transition: all 1s;
}

#back:hover {
  /* 颜色貌似不太对 */
  background-image: url(./assets/back.png), linear-gradient(#3298fe, #3298fe);
}

input[type='text'] {
  /* 去除点击时边框 */
  outline: none;
  cursor: default;
  width: 70%;
  height: 29px;
  border: 1px solid #d9d9d9;
  margin: 7px 14px 7px 3%;
}

#file {
  width: 20%;
  height: 29px;
  border: 2px dashed #dfdfdf;
  margin-bottom: -11px;
  display: inline-block;
  font-size: 18px;
  font-weight: 800;
  color: #999999;
  text-align: center;
}
</style>
