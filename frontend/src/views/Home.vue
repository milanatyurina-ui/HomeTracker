<script setup>

</script>

<template>

  <div class="wrapper">
    <header>
      <div class="container">
        <div class="left-part">
          <span class="Logo">Трекер домашних дел</span>
          <nav class="main-nav">
            <ul>
              <li>Мои задачи</li>
              <li>Категории задач</li>
              <li class="btn"><button>+</button></li>
              <li class="btn"><button>+</button></li>
            </ul>
          </nav>
        </div>
      </div>
    </header>
  </div>

  <div class="wrapper">
    <div class="main-content">
      <ul class="task-list">
        <li class="task-item">
          <article class="task-card">
            <h3>Убраться дома</h3>
            <h3>Протереть пыль</h3>

            <div class="stars">
              <button>☆</button>
              <button>☆</button>
              <button>☆</button>
            </div>

            <time datetime="2025-05-25T12:00">25.05 12:00</time>
            <input type="checkbox">

          </article>
        </li>
      </ul>
    </div>
  </div>



</template>

<style scoped>

</style>