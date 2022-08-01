import { mount } from '@vue/test-utils';
import MapDisplay from '@components/MapDisplay.vue'


import { shallowMount } from '@vue/test-utils'
import MapDisplay from '@/components/MapDisplay.vue'

describe('MapDisplay.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message'
    const wrapper = shallowMount(MapDisplay, {
      props: { msg }
    })
    expect(wrapper.text()).toMatch(msg)
  })
})
