/// <reference types="google.maps" />
import { PropType } from "vue";
declare const _default: import("vue").DefineComponent<{
    apiPromise: {
        type: PropType<Promise<typeof google>>;
    };
    apiKey: {
        type: StringConstructor;
        default: string;
    };
    version: {
        type: StringConstructor;
        default: string;
    };
    libraries: {
        type: PropType<("drawing" | "geometry" | "localContext" | "places" | "visualization")[]>;
        default: () => string[];
    };
    region: {
        type: StringConstructor;
        required: false;
    };
    language: {
        type: StringConstructor;
        required: false;
    };
    backgroundColor: {
        type: StringConstructor;
        required: false;
    };
    center: {
        type: PropType<google.maps.LatLng | google.maps.LatLngLiteral>;
        default: () => {
            lat: number;
            lng: number;
        };
    };
    clickableIcons: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    controlSize: {
        type: NumberConstructor;
        required: false;
    };
    disableDefaultUi: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    disableDoubleClickZoom: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    draggable: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    draggableCursor: {
        type: StringConstructor;
        required: false;
    };
    draggingCursor: {
        type: StringConstructor;
        required: false;
    };
    fullscreenControl: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    fullscreenControlPosition: {
        type: PropType<"BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT">;
        required: false;
    };
    gestureHandling: {
        type: PropType<"cooperative" | "greedy" | "none" | "auto">;
        required: false;
    };
    heading: {
        type: NumberConstructor;
        required: false;
    };
    keyboardShortcuts: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    mapTypeControl: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    mapTypeControlOptions: {
        type: PropType<google.maps.MapTypeControlOptions>;
        required: false;
    };
    mapTypeId: {
        type: PropType<string>;
        required: false;
    };
    mapId: {
        type: StringConstructor;
        required: false;
    };
    maxZoom: {
        type: NumberConstructor;
        required: false;
    };
    minZoom: {
        type: NumberConstructor;
        required: false;
    };
    noClear: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    panControl: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    panControlPosition: {
        type: PropType<"BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT">;
        required: false;
    };
    restriction: {
        type: PropType<google.maps.MapRestriction>;
        required: false;
    };
    rotateControl: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    rotateControlPosition: {
        type: PropType<"BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT">;
        required: false;
    };
    scaleControl: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    scaleControlStyle: {
        type: PropType<google.maps.ScaleControlStyle>;
        required: false;
    };
    scrollwheel: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    streetView: {
        type: PropType<google.maps.StreetViewPanorama>;
        required: false;
    };
    streetViewControl: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    streetViewControlPosition: {
        type: PropType<"BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT">;
        required: false;
    };
    styles: {
        type: PropType<google.maps.MapTypeStyle[]>;
        required: false;
    };
    tilt: {
        type: NumberConstructor;
        required: false;
    };
    zoom: {
        type: NumberConstructor;
        required: false;
    };
    zoomControl: {
        type: BooleanConstructor;
        required: false;
        default: undefined;
    };
    zoomControlPosition: {
        type: PropType<"BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT">;
        required: false;
    };
}, {
    mapRef: import("vue").Ref<HTMLElement | undefined>;
    ready: import("vue").Ref<boolean>;
    map: import("vue").Ref<google.maps.Map | undefined>;
    api: import("vue").Ref<typeof google.maps | undefined>;
    mapTilesLoaded: import("vue").Ref<boolean>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, string[], string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<{
    apiKey: string;
    version: string;
    libraries: ("drawing" | "geometry" | "localContext" | "places" | "visualization")[];
    center: google.maps.LatLng | google.maps.LatLngLiteral;
    clickableIcons: boolean;
    disableDefaultUi: boolean;
    disableDoubleClickZoom: boolean;
    draggable: boolean;
    fullscreenControl: boolean;
    keyboardShortcuts: boolean;
    mapTypeControl: boolean;
    noClear: boolean;
    panControl: boolean;
    rotateControl: boolean;
    scaleControl: boolean;
    scrollwheel: boolean;
    streetViewControl: boolean;
    zoomControl: boolean;
} & {
    apiPromise?: Promise<typeof google> | undefined;
    region?: string | undefined;
    language?: string | undefined;
    backgroundColor?: string | undefined;
    controlSize?: number | undefined;
    draggableCursor?: string | undefined;
    draggingCursor?: string | undefined;
    fullscreenControlPosition?: "BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT" | undefined;
    gestureHandling?: "cooperative" | "greedy" | "none" | "auto" | undefined;
    heading?: number | undefined;
    mapTypeControlOptions?: google.maps.MapTypeControlOptions | undefined;
    mapTypeId?: string | undefined;
    mapId?: string | undefined;
    maxZoom?: number | undefined;
    minZoom?: number | undefined;
    panControlPosition?: "BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT" | undefined;
    restriction?: google.maps.MapRestriction | undefined;
    rotateControlPosition?: "BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT" | undefined;
    scaleControlStyle?: google.maps.ScaleControlStyle | undefined;
    streetView?: google.maps.StreetViewPanorama | undefined;
    streetViewControlPosition?: "BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT" | undefined;
    styles?: google.maps.MapTypeStyle[] | undefined;
    tilt?: number | undefined;
    zoom?: number | undefined;
    zoomControlPosition?: "BOTTOM_CENTER" | "BOTTOM_LEFT" | "BOTTOM_RIGHT" | "LEFT_BOTTOM" | "LEFT_CENTER" | "LEFT_TOP" | "RIGHT_BOTTOM" | "RIGHT_CENTER" | "RIGHT_TOP" | "TOP_CENTER" | "TOP_LEFT" | "TOP_RIGHT" | undefined;
}>, {
    apiKey: string;
    version: string;
    libraries: ("drawing" | "geometry" | "localContext" | "places" | "visualization")[];
    center: google.maps.LatLng | google.maps.LatLngLiteral;
    clickableIcons: boolean;
    disableDefaultUi: boolean;
    disableDoubleClickZoom: boolean;
    draggable: boolean;
    fullscreenControl: boolean;
    keyboardShortcuts: boolean;
    mapTypeControl: boolean;
    noClear: boolean;
    panControl: boolean;
    rotateControl: boolean;
    scaleControl: boolean;
    scrollwheel: boolean;
    streetViewControl: boolean;
    zoomControl: boolean;
}>;
export default _default;
