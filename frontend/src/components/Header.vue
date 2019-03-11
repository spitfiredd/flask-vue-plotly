<template>
  <sui-menu fixed>
    <sui-menu-item name="Home"><router-link to="/">Home</router-link></sui-menu-item>
    <sui-dropdown item >Plots
      <sui-dropdown-menu>
        <sui-dropdown-item><router-link to="/plot">Hello Plot</router-link></sui-dropdown-item>
      </sui-dropdown-menu>
    </sui-dropdown>
  </sui-menu>
</template>
