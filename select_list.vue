<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Fail_List</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" @click="go">Back to Full List</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Year</th>
              <th scope="col">Month</th>
              <th scope="col">Day</th>
              <th scope="col">Hour</th>
              <th scope="col">Minute</th>
              <th scope="col">Second</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(select_each, index) in select_lists" :key="index">
              <td>{{ select_each.Year}}</td>
              <td>{{ select_each.Month}}</td>
              <td>{{ select_each.Day}}</td>
              <td>{{ select_each.Hour}}</td>
              <td>{{ select_each.Minute}}</td>
              <td>{{ select_each.Second}}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Inspect Log file</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      select_lists: [],
    };
  },
  methods: {
    go(){
      this.$router.push('/')
    },

    getLists() {
      const path = 'http://localhost:5000/fail';
      axios.get(path)
        .then((res) => {
          this.select_lists = res.data.fail;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getLists();
  },
};
</script>
