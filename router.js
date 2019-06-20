import Vue from 'vue';
import Router from 'vue-router';
import csv_list from './components/csv_list.vue';
import select_list from './components/select_list.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'csv_list',
      component: csv_list,
    },
    {
      path: '/fail',
      name: 'select_list',
      component: select_list,
    },
  ],
});
