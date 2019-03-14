<template>
  <nav class="navbar is-fixed-top" role="navigation" aria-label="main navigation">
    <div id="plotlyExamplesNavbar" class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/" class="navbar-item">
        Home
        </router-link>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            Example Plots
          </a>

          <div class="navbar-dropdown">
            <router-link to="/plot" class="navbar-item">
              Hello Plot
            </router-link>
            <router-link to="/autocorr" class="navbar-item">
              ACF
            </router-link>
            <router-link to="/monte" class="navbar-item">
              Monte Carlo
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
