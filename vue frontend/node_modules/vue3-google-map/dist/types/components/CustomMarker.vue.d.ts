/// <reference types="google.maps" />
import { PropType } from "vue";
declare const _default: import("vue").DefineComponent<{
    options: {
        type: PropType<google.maps.CustomMarkerOptions>;
        required: true;
    };
}, {
    customMarkerRef: import("vue").Ref<HTMLElement | undefined>;
    customMarker: import("vue").Ref<(google.maps.OverlayView & {
        getPosition(): google.maps.LatLng | null;
        getVisible(): boolean;
        setOptions(options: google.maps.CustomMarkerOptions): void;
    }) | undefined>;
    hasSlotContent: import("vue").ComputedRef<boolean | undefined>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, Record<string, any>, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<{
    options: google.maps.CustomMarkerOptions;
} & {}>, {}>;
export default _default;
