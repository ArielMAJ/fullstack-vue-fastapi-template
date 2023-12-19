<template>
  <div id="content">
    <p v-if="loadingMessage">Loading message...</p>
    <p v-else>{{ message }}</p>
    <p v-if="loadingRandomNumber">Loading random number...</p>
    <p v-else>Random Number: {{ formattedRandomNumber }}</p>
    <button
      @click="fetchRandomNumber"
      class="button"
      :disabled="loadingRandomNumber"
    >
      Update Random Number
    </button>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      message: "",
      randomNumber: null,
      loadingMessage: true,
      loadingRandomNumber: true,
    };
  },
  computed: {
    formattedRandomNumber() {
      return String(this.randomNumber).padStart(5, "0");
    },
  },
  mounted() {
    this.fetchMessage();
    this.fetchRandomNumber();
  },
  methods: {
    async fetchMessage() {
      try {
        this.loadingMessage = true;
        const response = await fetch(process.env.VUE_APP_BACKEND_ROOT_ENDPOINT);
        const data = await response.json();
        this.message = data.message;
        this.loadingMessage = false;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
    async fetchRandomNumber() {
      try {
        this.loadingRandomNumber = true;
        const response = await fetch(
          process.env.VUE_APP_BACKEND_ROOT_ENDPOINT + "random"
        );
        const data = await response.json();
        this.randomNumber = data.message.toFixed(2);
        this.loadingRandomNumber = false;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
/* Add your scoped styles here */
#content {
  display: flex;
  flex-direction: column;
  border: 1px solid black;
  border-radius: 20px;
  margin: auto;
  margin-top: 10%;
  padding: 10px;
  width: fit-content;
  min-width: 400px;
  min-height: 100px;
  text-align: center;
  align-items: center;
  justify-content: space-around;
}

.button {
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 10px;
  cursor: pointer;
  border: 3px double #4caf50;
  transition-duration: 0.4s;
  background-color: #c1eec2;
  color: black;

  &:hover {
    color: white;
    background-color: #4caf50;
  }

  &:active {
    transform: scale(0.95);
  }

  &:disabled {
    cursor: not-allowed;
    background-color: #ccc;
    border-color: #aaa;
    color: #888;
  }
}
</style>
