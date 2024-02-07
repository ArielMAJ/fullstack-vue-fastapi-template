<template>
  <v-app-bar :elevation="2" location="top">
    <!--
    <template v-slot:prepend>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
    </template>
    -->
    <v-app-bar-title> Application Bar </v-app-bar-title>

    <template v-slot:append>
      <v-btn icon="mdi-view-dashboard" to="/"></v-btn>
      <v-btn icon="mdi-approximately-equal-box" to="/double-random"></v-btn>
    </template>
  </v-app-bar>
</template>

<script lang="ts" setup>
//
</script>
