<template>
  <div>
    <el-container>
      <el-header>
        Todo app
      </el-header>
      <el-form
          @submit.native.prevent="addTask"
          ref="form"
          :inline="true"
          :model="form"
          label-width="80px"
          label-position="left"
          style="margin-left: 20px;margin-top: 30px;"
      >
        <el-form-item label="Add task">
          <el-input v-model="form.name" placeholder="Task title"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="addTask">Add</el-button>
        </el-form-item>
      </el-form>
      <p>Tasks</p>
      <div v-loading="loading">
        <el-card
            v-for="todo in todos"
            :key="todo.index"
        >
          {{ todo.title }}
          <div
              style="float: right; height: 10px; width: 10px; border-radius: 100%"
              @click="changeTask(todo.id)"
              :class="[{'green-dot': todo.done}, {'red-dot': !todo.done}]"
          ></div>
          <i
              class="el-icon-delete"
              @click="dialogVisibleHandle(todo.title ,todo.id)"
              style="float: right; margin-right: 10px;"
          ></i>
        </el-card>
      </div>
      <el-dialog
          title="Tips"
          :visible.sync="dialogVisible"
          width="80%">
        <span>Are you sure to delete item {{ itemWillDelete }}</span>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">Cancel</el-button>
            <el-button type="primary" @click="deleteItem">Confirm</el-button>
          </span>
      </el-dialog>
    </el-container>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data: () => ({
    todos: [],
    dialogVisible: false,
    deleteId: null,
    itemWillDelete: null,
    loading: false,
    form: {
      name: ''
    }
  }),
  methods: {
    async changeTask(id) {
      try {
        this.loading = true
        let idx = this.todos.findIndex((key) => {
          return key.id === id
        })
        await fetch(`http://127.0.0.1:8000/api/v1/${id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            done: !this.todos[idx].done
          })
        })

        this.todos[idx].done = !this.todos[idx].done
      } catch (error) {
        console.error('Ошибка:', error);
      }
      this.dialogVisible = false
      this.loading = false
    },
    dialogVisibleHandle(name ,id) {
      this.deleteId = id
      this.itemWillDelete = name
      this.dialogVisible = true
    },
    async deleteItem() {
      try {
        this.loading = true
        await fetch(`http://127.0.0.1:8000/api/v1/${this.deleteId}/`, {
          method: 'DELETE'
        })
        let id = this.todos.findIndex((key) => {
          return key.id === this.deleteId
        })
        this.todos.splice(id, 1)
      } catch (error) {
        console.error('Ошибка:', error);
      }
      this.dialogVisible = false
      this.loading = false
    },
    async addTask() {
      try {
        this.loading = true
        const response = await fetch('http://127.0.0.1:8000/api/v1/add/', {
          method: 'POST', // или 'PUT'
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            title: this.form.name
          })
        });
        const json = await response.json();
        this.todos.push(json)
        this.form.name = ''
        this.loading = false
      } catch (error) {
        console.error('Ошибка:', error);
        this.loading = false
      }
    }
  },
  created() {
    this.loading = true
    fetch('http://127.0.0.1:8000/api/v1/all/')
        .then(response => response.json())
        .then(json => {
          this.todos = json
          this.loading = false
        })
  }
}
</script>

<style scoped>
.el-header {
  font-family: Calibri, serif;
  font-size: 32px;
  box-shadow: 1px 1px 10px 1px #bab8b8;
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
.el-card {
  margin: 5px;
}

p {
  font-size: 30px;
  margin: 10px;
  font-family: Calibri, serif;
}

.green-dot {
  background: #0dcb0d;
}

.red-dot {
  background: red;
}
</style>
