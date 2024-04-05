<template>
  <div id="docker">
    <div class="top block">
      <div class="name">名称</div>
      <div class="time">创建日期</div>
      <div class="type">文件类型</div>
      <div class="size">大小</div>
    </div>
    <div v-for="(item, key, i) in object" :key="i">
      <div class="block" v-if="item.content" @click="$parent.path += item.info['fileName'] + '/'">
        <div class="folder"></div>
        <div class="name">{{ item.info['fileName'] }}</div>
        <!-- 占位符,功能之后实现 -->
        <div class="time">{{ new Date(item.info['createTime'] * 1000).format('yyyy-MM-dd hh:mm:ss') }}</div>
        <div class="type">文件夹</div>
      </div>
      <div class="block" v-else @contextmenu="'';">
        <div class="file"></div>
        <div class="name">{{ item.info['fileName'] }}</div>
        <div class="time">{{ new Date(item.info['createTime'] * 1000).format('yyyy-MM-dd hh:mm:ss') }}</div>
        <div class="type">文件</div>
        <div class="size">{{ sizeCount(item.info['size']) }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tree',
  data() {
    return {
      // Windows其实只存在KB单位
      dic: ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB'],
    };
  },
  props: ['object'],
  methods: {
    sizeCount(size) {
      let temp = size;
      let count = 0;
      while (temp >= 1024) {
        temp = temp / 1024;
        count++;
      }
      // Windows存在更加合理的对齐方式
      return String(temp).split('.')[0] + ' ' + this.dic[count];
    },
  },
};
</script>

<style>
.block {
  height: 22px;
  width: 100%;
  font-size: 13px;
  background-size: 100%;
}
.block > * {
  display: inline-block;
  /* 自由拖动,文本溢出时显示省略号 */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.top {
  margin: 15px 0 15px 5px;
  font-size: 12px;
  color: #4c607a;
}
/* 补差对齐 */
.top > .name {
  margin-right: 20px;
}
.top > *:not(.name) {
  padding-left: 5px;
  margin-left: calc(5% - 5px);
  border-left: 1px solid #e5e5e5;
}
.name {
  width: 55%;
}
.time,
.type,
.size {
  width: 130px;
  margin-left: 5%;
  color: #6d6d6d;
}
.folder,
.file {
  float: left;
  height: 20px;
  width: 25px;
  background-size: 100%;
}
.folder {
  background-image: url(../assets/folder.png);
}
.file {
  background-image: url(../assets/file.png);
}
</style>