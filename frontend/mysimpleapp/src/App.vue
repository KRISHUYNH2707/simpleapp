<template>
  <div>
    <h1>Items</h1>
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }} - {{ item.description }}
        <button @click="deleteItem(item.id)">Delete</button>
      </li>
    </ul>
    <input v-model="newItem.name" placeholder="Name" />
    <input v-model="newItem.description" placeholder="Description" />
    <button @click="addItem">Add Item</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      newItem: {
        name: '',
        description: ''
      }
    };
  },
  created() {
    this.fetchItems();
  },
  methods: {
    async fetchItems() {
      const response = await this.$axios.get('/items');
      this.items = response.data;
    },
    async addItem() {
      await this.$axios.post('/items', this.newItem);
      this.newItem = { name: '', description: '' };
      this.fetchItems();
    },
    async deleteItem(id) {
      await this.$axios.delete(`/items/${id}`);
      this.fetchItems();
    }
  }
};
</script>