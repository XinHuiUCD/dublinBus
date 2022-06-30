<template>
  <label class="open-weather-widget__toggle__container">
    <input 
      @change="$emit('input', $event.target.checked)"
      class="open-weather-widget__toggle__checkbox" 
      type="checkbox"
      :checked="$attrs.value"
    >
      <span class="open-weather-widget__toggle__button"></span>
      <span class="open-weather-widget__toggle__label">{{label}}</span>
  </label>
</template>

<script>
export default {
  name: 'Toggle',
  props: {
    label: String
  }
}
</script>

<style lang="scss" scoped>
.open-weather-widget__toggle__container {
  --voww-switch-container-width: 36px;
  --voww-switch-size: calc(var(--voww-switch-container-width) / 2);
}

.open-weather-widget {
  &__toggle {
    &__checkbox {
      width: 0px;
      height: 0px;
      &:checked + .open-weather-widget__toggle__button {
        background-color: rgba(var(--voww-accent-color-value), 1);
      }
      &:checked + .open-weather-widget__toggle__button::before {
        transform: translateX(
          calc(var(--voww-switch-container-width) - var(--voww-switch-size))
        );
      }
    }
    &__container {
      display: flex;
      align-items: center;
      cursor: pointer;
    }
    &__button {
      position: relative;
      display: flex;
      align-items: center;
      height: var(--voww-switch-size);
      flex-basis: var(--voww-switch-container-width);
      border-radius: var(--voww-switch-size);
      background-color: #dee4ec;
      transition: all 0.2s ease;
      &::before {
        content: "";
        position: absolute;
        left: 2px;
        height: calc(var(--voww-switch-size) - 4px);
        width: calc(var(--voww-switch-size) - 4px);
        border-radius: 100%;
        background-color: #fff;
        transition: all 0.2s ease;
      }
    }
    &__label {
      margin-left: 8px
    }
  }
}
</style>