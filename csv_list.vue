<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>CSV_List</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" @click="go">Find Failed Test</button>
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
            <tr v-for="(csv_each, index) in csv_lists" :key="index">
              <td>{{ csv_each.Year}}</td>
              <td>{{ csv_each.Month}}</td>
              <td>{{ csv_each.Day}}</td>
              <td>{{ csv_each.Hour}}</td>
              <td>{{ csv_each.Minute}}</td>
              <td>{{ csv_each.Second}}</td>
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
      csv_lists: [],
    };
  },
  methods: {
    go(){
      this.$router.push('/fail')
    },

    getLists() {
      const path = 'http://localhost:5000/all';
      axios.get(path)
        .then((res) => {
          this.csv_lists = res.data.all;
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
