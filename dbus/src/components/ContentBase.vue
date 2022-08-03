<template>
    <div class="home">
        <div class="container">
            <div class="card">
                <div class="card-body">
                    <slot></slot>
                </div>
            </div>
        </div>
        <footer style="text-align: center;margin-top: 10px;color: #1dc1ec">
            © 2022: XpressBusEgineering- Team 10
        </footer>
    </div>
</template>

<script lang="ts">
</script>

<style scoped>
.card-body {
    background: transparent;
}
</style>