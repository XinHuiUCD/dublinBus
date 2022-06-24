<template>
    <div class="home">
        <div class="container">
            <div class="card">
                <div class="card-body">
                    <slot></slot>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">

export default {
    name: "ContentBase",
    components: {
    }
}

</script>

<style scoped>
.card-body {
    background: whitesmoke;
}
</style>