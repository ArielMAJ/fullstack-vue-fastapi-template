<template>
  <div>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      message: "",
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        // Replace 'https://front-back-integration-template-arielmaj.vercel.app/' with your actual backend API endpoint
        const response = await fetch(
          "https://front-back-integration-template-arielmaj.vercel.app/"
        );
        const data = await response.json();
        this.message = data.message;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
  },
};
</script>

<style scoped>
/* Add your scoped styles here */
</style>
